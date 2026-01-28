import os

# Il tuo ID Affiliato che hai preso da Amazon
AMAZON_TAG = os.getenv('AMAZON_TAG')

def genera_link(url_prodotto):
    # Questa funzione aggiunge in automatico il tuo ID ai link
    if "?" in url_prodotto:
        return f"{url_prodotto}&tag={AMAZON_TAG}"
    else:
        return f"{url_prodotto}?tag={AMAZON_TAG}"

print("PALOXIS BOT ATTIVO")
# Qui in futuro aggiungeremo la lista dei prodotti dei tuoi video
test_url = "https://www.amazon.it/dp/B08PCYF3S8"
print(f"Link pronto per il guadagno: {genera_link(test_url)}")
