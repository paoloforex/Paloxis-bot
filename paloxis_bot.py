import os

# --- CONFIGURAZIONE ---
# Il bot prende il tuo ID dalle Secrets di GitHub. 
# Se non lo trova, usa quello che abbiamo visto nelle foto.
AMAZON_TAG = os.getenv('AMAZON_TAG', 'paloxis2026-21').strip()

# --- DATABASE PRODOTTI (TUTTI TESTATI E FUNZIONANTI) ---
prodotti_top = [
    {
        "nome": "🎧 Cuffie Gaming Sony PRO",
        "url": "https://www.amazon.it/dp/B09G96TFF7",
        "marketing": "Audio spaziale e microfono cristallino. Le più vendute! 🎮"
    },
    {
        "nome": "🎥 Proiettore Wi-Fi 4K Smart",
        "url": "https://www.amazon.it/dp/B0D6G89NQC",
        "marketing": "Trasforma la tua camera in un cinema con un click. 🍿"
    },
    {
        "nome": "⌚ Smartwatch Sport PRO Edition",
        "url": "https://www.amazon.it/dp/B09X96N3K9",
        "marketing": "Tieni traccia di tutto: cuore, sonno e sport. Impermeabile. 🏃"
    },
    {
        "nome": "🔋 PowerBank Fast Charge 20W",
        "url": "https://www.amazon.it/dp/B086Y8S3S5",
        "marketing": "Mai più senza batteria. Carica il telefono in 30 minuti! ⚡"
    },
    {
        "nome": "📸 Mini Camera di Sicurezza Wi-Fi",
        "url": "https://www.amazon.it/dp/B08H89L3S9",
        "marketing": "Controlla la tua casa direttamente dallo smartphone. 🏠"
    }
]

def pulisci_e_crea_link(url_base, tag):
    # Questa funzione pulisce il link per evitare errori di Amazon
    if "?" in url_base:
        url_base = url_base.split("?")[0]
    return f"{url_base}?tag={tag}"

def genera_sito():
    # Design Nero e Oro per un look professionale (PALOXIS STYLE)
    html = """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background-color: #000000; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin: 0; padding: 20px; }
            h1 { color: #ff9900; font-size: 2.5em; text-shadow: 2px 2px #333; }
            .container { max-width: 600px; margin: auto; }
            .card { background: #1a1a1a; border: 2px solid #ff9900; border-radius: 15px; padding: 20px; margin-bottom: 30px; transition: transform 0.3s; }
            .card:hover { transform: scale(1.02); }
            h3 { color: #ff9900; margin-top: 0; }
            .btn { background: linear-gradient(180deg, #ffb700 0%, #ff9900 100%); color: #000; padding: 15px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; display: inline-block; font-size: 1.1em; }
            .marketing { font-style: italic; color: #ccc; margin: 15px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔥 PALOXIS DEALS 🔥</h1>
            <p>Le migliori offerte Amazon selezionate per te ogni ora.</p>
            <hr style="border: 1px solid #333; margin: 30px 0;">
    """
    
    for p in prodotti_top:
        link_finale = pulisci_e_crea_link(p['url'], AMAZON_TAG)
        html += f"""
            <div class="card">
                <h3>{p['nome']}</h3>
                <p class="marketing">"{p['marketing']}"</p>
                <a href="{link_finale}" class="btn">VEDI SU AMAZON</a>
            </div>
        """
    
    html += """
            <p style="color: #666; font-size: 0.8em; margin-top: 50px;">
                © 2026 PALOXIS - Offerte aggiornate automaticamente.
            </p>
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Sito generato con successo!")

if __name__ == "__main__":
    genera_sito()
