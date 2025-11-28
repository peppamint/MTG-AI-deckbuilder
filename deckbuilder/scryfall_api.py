import requests # library to make HTTP requests to Scryfall's API

BASE_URL = "https://api.scryfall.com"

def search_cards(query, unique="cards"):
    """
    Query Scryfall with any string (e.g. 'type:creature color>=WU legal:standard').
    Returns all results (auto-pagination).
    """
    url = f"{BASE_URL}/cards/search"
    params = {"q": query, "unique": unique}
    cards = []

    while True:
        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json()

        cards.extend(data.get("data", []))

        if not data.get("has_more"):
            break
        url = data.get("next_page")

    return cards
