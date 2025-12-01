from deckbuilder.builder import build_deck

def format_deck(deck):
    out = []
    for card in deck["cards"]:
        out.append(card["name"])
    out.append(f"--- {deck['lands']} Lands Recommended ---")
    return "\n".join(out)

def main():
    raw_colors = input("Enter colors (comma separated letters, e.g. R,G,U):")
    colors = [c.strip() for c in raw_colors.split(",")]

    archetype = input("Enter corresponding number: 1 for aggro, 2 for midrange, 3 for control")

    budget = input("Enter budget in USD")

    # colors = ['R', 'G']
    # archetype = "aggro"
    # budget = False

    deck = build_deck(colors, archetype, budget)
    print(format_deck(deck))

if __name__ == "__main__":
    main()
