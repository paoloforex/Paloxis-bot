# --- DATABASE PRODOTTI TESTATI E FUNZIONANTI ---
prodotti_top = [
    {
        "nome": "🎥 Proiettore Portatile 4K",
        "url": "https://www.amazon.it/dp/B0CKR9V8M2",
        "marketing": "Il gadget più virale del momento! Cinema ovunque. 🍿"
    },
    {
        "nome": "🎧 Cuffie Bluetooth Noise Cancelling",
        "url": "https://www.amazon.it/dp/B09G96TFF7",
        "marketing": "Suono perfetto e batteria che dura giorni. ⭐"
    },
    {
        "nome": "🔋 PowerBank MagSafe Ultra",
        "url": "https://www.amazon.it/dp/B099279S8R",
        "marketing": "Ricarica il tuo iPhone senza cavi. Indispensabile. ⚡"
    }
]

def crea_link_diretto(url_base):
    # Rimuove eventuali spazi bianchi che rompono il link
    url_pulito = url_base.strip()
    tag_pulito = AMAZON_TAG.strip()
    return f"{url_pulito}?tag={tag_pulito}"
