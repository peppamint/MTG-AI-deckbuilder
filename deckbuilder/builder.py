from .scryfall_api import search_cards
from .heuristics import score_card, recommended_land_count

def build_deck(colors, archetype, budget=False):
    """
    colors: ['U','B']
    archetype: 'aggro' | 'midrange' | 'control'
    budget: ignore mythics/rares if True
    """

    color_query = "".join(colors)  # "RG"
    q = f"c>={color_query} legal:standard -type:land"

    if budget:
        q += " (rarity:c or rarity:u)"

    cards = search_cards(q)
    scored = sorted(cards, key=lambda c: score_card(c, archetype), reverse=True)

    deck = []
    lands = recommended_land_count(archetype)

    # simple rule: 60 cards, reserve slots for lands
    limit = 60 - lands

    for c in scored:
        if len(deck) >= limit:
            break
        deck.append(c)

    return {
        "cards": deck,
        "lands": lands,
    }
