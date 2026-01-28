import os

AMAZON_TAG = os.getenv('AMAZON_TAG')

# Lista prodotti con parole chiave per Google (SEO)
prodotti = [
    {"nome": "Proiettore 4K Portatile", "url": "https://www.amazon.it/dp/B0CKR9V8M2", "keyword": "miglior proiettore 2026 economico"},
    {"nome": "Cuffie Conduzione Ossea", "url": "https://www.amazon.it/dp/B09BVXT8TJ", "keyword": "cuffie sport invisibili amazon"},
    {"nome": "PowerBank MagSafe", "url": "https://www.amazon.it/dp/B09G96TFF7", "keyword": "caricatore iphone magnetico sottile"}
]

def crea_sito_calamitante():
    html = f"""
    <html>
    <head>
        <title>PALOXIS - Offerte Tech Tendenze 2026</title>
        <meta name="description" content="Scopri i prodotti più venduti su Amazon. Recensioni e offerte tech aggiornate ogni ora.">
        <style>
            body {{ font-family: 'Arial', sans-serif; background: #1a1a1a; color: white; text-align: center; }}
            .box {{ border: 2px solid #ff9900; margin: 20px; padding: 20px; border-radius: 20px; background: #222; }}
            a {{ color: #1a1a1a; background: #ff9900; padding: 15px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; display: inline-block; }}
        </style>
    </head>
    <body>
        <h1>🔥 PALOXIS: TRENDS DEL MOMENTO 🔥</h1>
        <p>Le migliori offerte selezionate automaticamente dalla nostra AI</p>
    """
    
    for p in prodotti:
        link = f"{p['url']}?tag={AMAZON_TAG}"
        html += f"""
        <div class="box">
            <h2>{p['nome']}</h2>
            <p>Ottimizzato per: {p['keyword']}</p>
            <a href="{link}">VEDI OFFERTA SU AMAZON</a>
        </div>
        """
    
    html += "</body></html>"
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    crea_sito_calamitante()
