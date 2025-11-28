def recommended_land_count(archetype):
    # simple first-pass
    if archetype == "aggro":
        return 22
    if archetype == "midrange":
        return 24
    if archetype == "control":
        return 26
    return 24

def score_card(card, archetype):
    """Return a numerical score. We keep it primitive to show the concept."""
    ctype = card.get("type_line", "").lower()
    oracle = card.get("oracle_text", "").lower()

    score = 0

    # general creature bias for aggro
    if archetype == "aggro" and "creature" in ctype:
        score += 3

    # control wants card draw & removal
    if archetype == "control":
        if "draw" in oracle:
            score += 3
        if "destroy" in oracle or "counter" in oracle:
            score += 4

    # midrange = flexible threats
    if archetype == "midrange":
        if "creature" in ctype:
            score += 2
        if "planeswalker" in ctype:
            score += 3

    # cheap mana = bonus
    cmc = card.get("cmc", 5)
    if cmc <= 3:
        score += 1

    # generic stat fallback
    return score
