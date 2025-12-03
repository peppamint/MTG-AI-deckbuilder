def tag_card(card):
    '''
    given a card, returns a list of its tags
    tag pool: 
    '''
    tags = []

    type_line = card.get("type_line", "").lower()
    oracle = card.get("oracle_text", "").lower()

    # type classification
    if "creature" in type_line:
        tags.append("creature")
    if "planeswalker" in type_line:
        tags.append("planeswalker")
    if "artifact" in type_line:
        tags.append("artifact")
    if "enchantment" in type_line:
        tags.append("enchantment")

    if "draw a card" in oracle or "draw cards" in oracle:
        tags.append("draw")

    # removal keywords
    if "destroy target" in oracle or "exile target" in oracle:
        tags.append("removal")

    # token generation
    if "create" in oracle or "token" in oracle:
        tags.append("tokens")

    # lifegain
    if "gain" in oracle and "life" in oracle:
        tags.append("lifegain")
    if "lifelink" in oracle:
        tags.append("lifegain")

    # burn / direct damage
    if "deals" in oracle and "damage" in oracle:
        tags.append("burn")

    # counters
    if "+1/+1 counter" in oracle:
        tags.append("counters")
    
    if "proliferate" in oracle:
        tags.append("proliferate")
    
    # sacrifice
    if "sacrifice" or "whenever a creature you control dies" in oracle:
        tags.append("sacrifice")
    
    # death trigger
    if "dies" in oracle:
        tags.append("death_trigger")
    
    # use again
    if "return" in oracle and "graveyard" in oracle:
        tags.append("recursion")

    if "flashback" in oracle:
        tags.append("flashback")

    if "warp" in oracle:
        tags.append("warp")

    return list(dict.fromkeys(tags)) # involve dict b/c it preserves uniqueness