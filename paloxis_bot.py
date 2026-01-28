import os

AMAZON_TAG = os.getenv('AMAZON_TAG', 'paloxis2026-21').strip()

# --- PRODOTTI E CATEGORIE ---
# Ho cambiato i link dei prodotti mettendoli nel formato più semplice possibile (ASIN)
prodotti_top = [
    {"nome": "🎧 Cuffie Sony Wireless", "id": "B09G96TFF7"},
    {"nome": "🔋 PowerBank Fast Charge", "id": "B086Y8S3S5"},
    {"nome": "📺 Fire TV Stick 4K", "id": "B0CLDP6TTC"},
    {"nome": "⌚ Smartwatch Sport", "id": "B09X96N3K9"}
]

categorie_top = [
    {"nome": "🔥 TUTTE LE OFFERTE DEL GIORNO", "url": "https://www.amazon.it/gp/goldbox"},
    {"nome": "💻 TECH E INFORMATICA", "url": "https://www.amazon.it/b?node=425916031"}
]

def crea_link_prodotto(asin, tag):
    # Formato link più sicuro in assoluto per i prodotti
    return f"https://www.amazon.it/dp/{asin}?tag={tag}"

def crea_link_categoria(url_base, tag):
    # Formato per le categorie
    char = "&" if "?" in url_base else "?"
    return f"{url_base}{char}tag={tag}"

def genera_sito():
    html = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 20px; }
            .btn { background: #ff9900; color: #000; padding: 18px; margin: 12px auto; display: block; text-decoration: none; border-radius: 12px; font-weight: bold; max-width: 400px; }
            .cat { background: #222; color: #ff9900; border: 2px solid #ff9900; }
            h2 { color: #ff9900; margin-top: 40px; border-bottom: 1px solid #333; padding-bottom: 10px; }
        </style>
    </head>
    <body>
        <h1 style="color:#ff9900;">👑 PALOXIS DEALS 👑</h1>
        <p>Le offerte migliori caricate per te.</p>
        
        <h2>💎 PRODOTTI SCELTI</h2>
    """
    # Genera Bottoni Prodotti
    for p in prodotti_top:
        link = crea_link_prodotto(p['id'], AMAZON_TAG)
        html += f'<a href="{link}" class="btn">{p["nome"]}</a>'
    
    html += "<h2>📂 ESPLORA CATEGORIE</h2>"
    # Genera Bottoni Categorie
    for c in categorie_top:
        link = crea_link_categoria(c['url'], AMAZON_TAG)
        html += f'<a href="{link}" class="btn cat">{c["nome"]}</a>'
    
    html += "<p style='margin-top:50px; color:#555;'>Aggiornato in tempo reale dal Bot di Paloxis</p>"
    html += "</body></html>"
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    genera_sito()
