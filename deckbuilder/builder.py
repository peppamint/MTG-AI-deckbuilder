from .scryfall_api import search_cards
from .heuristics import score_card, recommended_land_count

def build_deck(colors, archetype, budget):

    color_query = "".join(colors)
    q = f"c>={color_query} legal:standard -type:land"

    cards = search_cards(q)

    deck = []
    total_cost = 0
    lands = recommended_land_count(archetype)

    scored = sorted(cards, key=lambda c: score_card(c, archetype, total_cost, budget), reverse=True)

    limit = 60 - lands

    for card in scored:
        
        price = card.get("prices", {}).get("usd")
        price = 0 if price is None else float(price)

        # Skip if adding card exceeds budget
        if total_cost + price > float(budget):
            continue

        deck.append(card)
        total_cost += price

        # Stop if hit deck limit
        if len(deck) >= limit:
            break

    return {
        "cards": deck,
        "lands": lands,
    }
