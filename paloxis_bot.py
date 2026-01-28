import os

AMAZON_TAG = os.getenv('AMAZON_TAG')

# Database Prodotti con Sconti e Trend 2026
prodotti_vincenti = [
    {"nome": "🎥 Proiettore Smart 4K Cinema", "prezzo": "89,90€", "sconto": "55%", "url": "https://www.amazon.it/dp/B0CKR9V8M2"},
    {"nome": "🎧 Cuffie Gaming Noise Cancelling", "prezzo": "45,00€", "sconto": "40%", "url": "https://www.amazon.it/dp/B09BVXT8TJ"},
    {"nome": "🔋 PowerBank MagSafe 20.000mAh", "prezzo": "29,99€", "sconto": "50%", "url": "https://www.amazon.it/dp/B09G96TFF7"},
    {"nome": "⌚ Smartwatch Sport GPS Pro", "prezzo": "34,50€", "sconto": "60%", "url": "https://www.amazon.it/dp/B09NR6Z67G"},
    {"nome": "🧹 Robot Aspirapolvere AI", "prezzo": "199,00€", "sconto": "45%", "url": "https://www.amazon.it/dp/B0BSHF7WHH"}
]

def genera_sito():
    html = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PALOXIS - Offerte Lampo 2026</title>
        <style>
            body {{ font-family: sans-serif; background: #121212; color: white; margin: 0; padding: 20px; }}
            .header {{ background: #ff9900; padding: 30px; border-radius: 20px; text-align: center; margin-bottom: 30px; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }}
            .card {{ background: #1e1e1e; border: 2px solid #333; padding: 20px; border-radius: 20px; text-align: center; }}
            .card:hover {{ border-color: #ff9900; }}
            .prezzo {{ font-size: 1.8em; color: #ff9900; font-weight: bold; }}
            .sconto {{ background: red; color: white; padding: 5px; border-radius: 5px; font-weight: bold; }}
            a {{ display: block; background: #ff9900; color: black; padding: 15px; text-decoration: none; border-radius: 10px; font-weight: bold; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🔥 PALOXIS DEALS 🔥</h1>
            <p>I prezzi più bassi di Amazon aggiornati ogni ora</p>
        </div>
        <h2 style="color: #ff4444; text-align: center;">⚡ SCONTI LAMPO DEL MOMENTO</h2>
        <div class="grid">
    """
    for p in prodotti_vincenti:
        link = f"{p['url']}?tag={AMAZON_TAG}"
        html += f"""
            <div class="card">
                <h3>{p['nome']}</h3>
                <p class="prezzo">{p['prezzo']}</p>
                <p><span class="sconto">SCONTO {p['sconto']}</span></p>
                <a href="{link}" target="_blank">COMPRA SU AMAZON</a>
            </div>
        """
    html += "</div></body></html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    genera_sito()
