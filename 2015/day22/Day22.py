import copy

SPELLS = {
    "Magic Missile": {"cost": 53, "damage": 4, "heal": 0, "duration": 0},
    "Drain": {"cost": 73, "damage": 2, "heal": 2, "duration": 0},
    "Shield": {"cost": 113, "armor": 7, "duration": 6},
    "Poison": {"cost": 173, "damage": 3, "duration": 6},
    "Recharge": {"cost": 229, "mana": 101, "duration": 5},
}

# Global variable to track the minimum mana spent
min_mana_spent = float("inf")

# Initial game state
initial_state = {
    "hp": 50,
    "mana": 500,
    "boss_hp": 58,
    "boss_damage": 9,
    "armor": 0,
    "effects": {},  # Active effects (spell: (turns left, value))
    "mana_spent": 0
}


def apply_effects(state):
    """Applies all active effects at the start of a turn."""
    new_state = copy.deepcopy(state)
    expired_effects = []



    for spell, (timer,value) in new_state["effects"].items():
        if timer>0:
            if spell=="Shield":
                new_state["armor"] = 7
            elif spell == "Poison":
                new_state["boss_hp"] -=3
            elif spell =="Recharge":
                new_state["mana"] +=101
        # Reduce duration
        new_state["effects"][spell] = (timer-1,value)
        if new_state["effects"][spell][0] ==0:
            expired_effects.append(spell)
    # Remove expired effects
    for effect in expired_effects:
        del new_state["effects"][effect]
        if effect=="Shield":
            new_state["armor"] = 0

    return new_state


def dfs(state,hardMode):
    """Recursive DFS to explore all possible spell sequences."""
    global min_mana_spent

    if hardMode:
        state["hp"]-=1
        if state["hp"] <=0:
            return

    # Apply effects at the start of the player's turn
    state = apply_effects(state)

    # If the boss is already dead after effects, update min_mana_spent and stop
    if state["boss_hp"]<=0:
        min_mana_spent = min(min_mana_spent, state["mana_spent"])
        return

    # Try casting each spell
    for spell, details in SPELLS.items():
        if spell in state["effects"]:
            continue
        if state["mana"]< details["cost"]:
            continue
        if details["cost"] + state["mana_spent"] >= min_mana_spent:
            continue

        # Create new state for the next move
        new_state = copy.deepcopy(state)
        new_state["mana"] -=details["cost"]
        new_state["mana_spent"] += details["cost"]

        if details["duration"] > 0:
            new_state["effects"][spell] = (details["duration"], 0)
        else:
            new_state["boss_hp"] -= details["damage"]
            new_state["hp"] += details["heal"]

        new_state = apply_effects(new_state)  # Apply effects after spell cast

        # If boss is dead after applying effects, update min mana and stop
        if new_state["boss_hp"]<=0:
            min_mana_spent = min(min_mana_spent, new_state["mana_spent"])
            continue

        # Boss attacks
        boss_damage = max(1,state["boss_damage"]-new_state["armor"])
        new_state["hp"] -=boss_damage

        # If wizard survives, continue search
        if new_state["hp"]>0:
            dfs(new_state,hardMode)


if __name__=='__main__':
    # Part 1:
    min_mana_spent = float('inf')  # Reset for part 2
    dfs(initial_state, False)
    print("Minimum mana spent (Part 1):", min_mana_spent)

    # Part 2:
    min_mana_spent = float('inf')  # Reset for part 2
    dfs(initial_state, True)
    print("Minimum mana spent (Part 2):", min_mana_spent)