import logging
from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, load_to_postgresql

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def scrape_all_products(base_url: str, max_pages: int = 50):
    all_products = []
    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else f"{base_url}page{page}"
        logging.info(f"Scraping halaman {page}: {url}")
        try:
            products = scrape_main(url)
            all_products.extend(products)
        except Exception as e:
            logging.warning(f"Gagal scrape halaman {page}: {e}")
    logging.info(f"Total produk berhasil di-scrape: {len(all_products)}")
    return all_products

def main():
    base_url = 'https://fashion-studio.dicoding.dev/'

    # Ekstraksi
    all_products = scrape_all_products(base_url)

    if not all_products:
        logging.error("Tidak ada produk yang berhasil di-scrape. ETL dibatalkan.")
        return

    # Transformasi
    try:
        df = transform_data(all_products)
    except Exception as e:
        logging.error(f"Gagal dalam proses transformasi: {e}")
        return

    # Load: ke CSV, PostgreSQL, dan Google Sheets
    save_to_csv(df)

    load_to_postgresql(df, table_name='products')

    save_to_google_sheets(
        df,
        spreadsheet_id='18tcdahc37EF19bPzHk77YcSpe1Yhx6oRUbF-yNMJNVM',
        range_name='Sheet1!A1'
    )

if __name__ == '__main__':
    main()