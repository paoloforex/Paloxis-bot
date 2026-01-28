import os

AMAZON_TAG = os.getenv('AMAZON_TAG', 'paloxis2026-21').strip()

# --- CATEGORIE IMMORTALI (NON SCADONO MAI) ---
categorie_top = [
    {"nome": "🔥 TUTTE LE OFFERTE DEL GIORNO", "url": "https://www.amazon.it/gp/goldbox"},
    {"nome": "💻 TECH E INFORMATICA", "url": "https://www.amazon.it/b?node=425916031"},
    {"nome": "🏠 CASA E CUCINA", "url": "https://www.amazon.it/b?node=524012031"},
    {"nome": "👕 MODA E ABBIGLIAMENTO", "url": "https://www.amazon.it/b?node=2454148031"}
]

# --- PRODOTTI BESTSELLER ---
prodotti_top = [
    {"nome": "🎧 Cuffie Sony Wireless", "url": "https://www.amazon.it/dp/B09G96TFF7"},
    {"nome": "🔋 PowerBank Ultra-Rapido", "url": "https://www.amazon.it/dp/B086Y8S3S5"},
    {"nome": "📺 Fire TV Stick 4K", "url": "https://www.amazon.it/dp/B0CLDP6TTC"}
]

def crea_link(url_base, tag):
    char = "&" if "?" in url_base else "?"
    return f"{url_base}{char}tag={tag}"

def genera_sito():
    html = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 20px; }
            .btn { background: #ff9900; color: #000; padding: 15px; margin: 10px; display: block; text-decoration: none; border-radius: 10px; font-weight: bold; }
            .cat { background: #333; color: #ff9900; border: 1px solid #ff9900; }
            h2 { color: #ff9900; margin-top: 40px; }
        </style>
    </head>
    <body>
        <h1>👑 PALOXIS EXCLUSIVE 👑</h1>
        <p>Clicca e approfitta degli sconti Amazon di oggi!</p>
        
        <h2>📂 CATEGORIE IN SCONTO</h2>
    """
    for c in categorie_top:
        html += f'<a href="{crea_link(c["url"], AMAZON_TAG)}" class="btn cat">{c["nome"]}</a>'
    
    html += "<h2>💎 PRODOTTI TOP</h2>"
    for p in prodotti_top:
        html += f'<a href="{crea_link(p["url"], AMAZON_TAG)}" class="btn">{p["nome"]}</a>'
    
    html += "</body></html>"
    with open("index.html", "w", encoding="utf-8") as f: f.write(html)

if __name__ == "__main__": genera_sito()
