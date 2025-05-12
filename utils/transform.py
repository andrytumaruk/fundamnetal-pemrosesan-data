import pandas as pd
from datetime import datetime

def transform_data(data):
    if not data:
        return pd.DataFrame(columns=['title', 'price', 'rating', 'colors', 'size', 'gender', 'timestamp'])

    df = pd.DataFrame(data)

    # Bersihkan kolom
    try:
        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    except Exception:
        return pd.DataFrame()

    # Drop jika rating atau price tidak valid
    df = df.dropna(subset=['price', 'rating'])

    # Bersihkan teks dari prefix
    for col in ['colors', 'size', 'gender']:
        df[col] = df[col].str.replace(r'^\w+: ', '', regex=True)

    # Drop jika title mengandung 'unknown'
    if 'title' in df.columns:
        df = df[~df['title'].str.lower().str.contains('unknown', na=False)]

    df['timestamp'] = datetime.now().isoformat()
    return df