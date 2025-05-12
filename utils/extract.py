import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_main(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Gagal mengakses URL: {url}. Detail: {e}")

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []

        cards = soup.find_all('div', class_='collection-card')
        for card in cards:
            def get_text(selector, keyword=None):
                if keyword:
                    tag = card.find('p', string=lambda text: text and keyword in text)
                else:
                    tag = card.find(*selector)
                return tag.text.strip() if tag else f'Tidak ada {keyword or selector[1]}'

            product = {
                'title': get_text(('h3', 'product-title'), None).replace('Tidak ada product-title', 'Unknown Title'),
                'price': get_text(('div', 'price-container'), None).replace('Tidak ada price-container', 'Price Unavailable'),
                'rating': get_text(None, 'Rating'),
                'colors': get_text(None, 'Colors'),
                'size': get_text(None, 'Size'),
                'gender': get_text(None, 'Gender'),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            products.append(product)

        print(f"✔ Berhasil scrape {len(products)} produk dari {url}")
        return products

    except Exception as e:
        raise Exception(f"Gagal parsing HTML dari {url}. Detail: {e}")