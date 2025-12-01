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

    

    archetype = "aggro"
    budget = False

    deck = build_deck(colors, archetype, budget)
    print(format_deck(deck))

if __name__ == "__main__":
    main()
