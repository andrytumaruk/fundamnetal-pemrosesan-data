import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine


def save_to_csv(df: pd.DataFrame, filename: str = "products.csv") -> None:
    """Simpan DataFrame ke file CSV."""
    try:
        df.to_csv(filename, index=False)
        print(f"✔ Data berhasil disimpan ke CSV: {filename}")
    except Exception as e:
        print(f"❌ Gagal menyimpan ke CSV: {e}")


def save_to_google_sheets(df: pd.DataFrame, spreadsheet_id: str, range_name: str) -> None:
    """Simpan DataFrame ke Google Sheets."""
    try:
        creds = Credentials.from_service_account_file('productfashion-459614-1f77a98b1ce4.json')
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        values = [df.columns.tolist()] + df.values.tolist()
        body = {'values': values}

        sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()

        print(f"✔ Data berhasil disimpan ke Google Sheets: {spreadsheet_id}")
    except Exception as e:
        print(f"❌ Gagal menyimpan ke Google Sheets: {e}")


def load_to_postgresql(df: pd.DataFrame, table_name: str = 'products') -> None:
    """Simpan DataFrame ke PostgreSQL."""
    try:
        db_config = {
            'username': 'postgres',
            'password': 'Zeronime09',
            'host': 'localhost',
            'port': '5432',
            'database': 'db_fashion',
        }

        engine_url = (
            f"postgresql+psycopg2://{db_config['username']}:{db_config['password']}"
            f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )
        engine = create_engine(engine_url)

        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"✔ Data berhasil disimpan ke PostgreSQL table '{table_name}'")
    except Exception as e:
        print(f"❌ Gagal menyimpan ke PostgreSQL: {e}")