import os

# --- PRELIEVO CREDENZIALI ---
AMAZON_TAG = os.getenv('AMAZON_TAG', 'paloxis2026-21').strip()

# --- DATABASE PRODOTTI (LINK SEMPLIFICATI) ---
prodotti_top = [
    {"nome": "Proiettore 4K", "url": "https://www.amazon.it/dp/B0CKR9V8M2"},
    {"nome": "Cuffie Tech", "url": "https://www.amazon.it/dp/B09G96TFF7"},
    {"nome": "Powerbank", "url": "https://www.amazon.it/dp/B099279S8R"}
]

def pulisci_e_crea_link(url_base, tag):
    # Rimuove tutto quello che c'è dopo il codice prodotto (dp/ASIN)
    # per evitare conflitti con il tuo tag
    if "?" in url_base:
        url_base = url_base.split("?")[0]
    return f"{url_base}?tag={tag}"

def genera_sito():
    html = "<html><body style='background:#121212;color:white;text-align:center;font-family:sans-serif;'>"
    html += "<h1>🔥 PALOXIS DEALS 🔥</h1>"
    
    for p in prodotti_top:
        link_finale = pulisci_e_crea_link(p['url'], AMAZON_TAG)
        html += f"""
        <div style='border:1px solid #ff9900;margin:20px;padding:20px;border-radius:15px;'>
            <h3>{p['nome']}</h3>
            <a href='{link_finale}' style='background:#ff9900;color:black;padding:10px 20px;text-decoration:none;border-radius:5px;font-weight:bold;'>VEDI SU AMAZON</a>
            <p style='font-size:10px;color:gray;'>Link: {link_finale}</p>
        </div>
        """
    
    html += "</body></html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    genera_sito()
