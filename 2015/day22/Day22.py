import copy

min_mana_spent = float('inf')

SPELLS = {
    "Magic Missile": {"cost": 53, "damage": 4, "heal": 0, "duration": 0},
    "Drain": {"cost": 73, "damage": 2, "heal": 2, "duration": 0},
    "Shield": {"cost": 113, "armor": 7, "duration": 6},
    "Poison": {"cost": 173, "damage": 3, "duration": 6},
    "Recharge": {"cost": 229, "mana": 101, "duration": 5},
}

def apply_effects(state):
    new_state = copy.deepcopy(state)
    to_remove = []

    for effect, (timer, value) in new_state["effects"].items():
        if timer > 0:
            if effect == "Shield":
                new_state["armor"] = 7
            elif effect == "Poison":
                new_state["boss_hp"] -= 3
            elif effect == "Recharge":
                new_state["mana"] += 101

            new_state["effects"][effect] = (timer - 1, value)
            if new_state["effects"][effect][0] == 0:
                to_remove.append(effect)

    for effect in to_remove:
        del new_state["effects"][effect]
        if effect == "Shield":
            new_state["armor"] = 0

    return new_state

def dfs(state):
    global min_mana_spent

    state = apply_effects(state)  # Apply effects at the start of the player's turn

    if state["boss_hp"] <= 0:
        min_mana_spent = min(min_mana_spent, state["mana_spent"])
        return

    for spell, details in SPELLS.items():
        if spell in state["effects"] and spell != "Recharge": # can recast recharge
            continue
        if state["mana"] < details["cost"]:
            continue
        if state["mana_spent"] + details["cost"] >= min_mana_spent:  # Pruning
            continue

        new_state = copy.deepcopy(state)
        new_state["mana"] -= details["cost"]
        new_state["mana_spent"] += details["cost"]

        if details["duration"] > 0:
            new_state["effects"][spell] = (details["duration"], 0)
        else:
            new_state["boss_hp"] -= details["damage"]
            new_state["hp"] += details["heal"]

        new_state = apply_effects(new_state)  # Apply effects after spell cast

        if new_state["boss_hp"] <= 0:
            min_mana_spent = min(min_mana_spent, new_state["mana_spent"])
            continue

        boss_damage = max(1, state["boss_damage"] - new_state["armor"])  # Use new_state armor
        new_state["hp"] -= boss_damage

        if new_state["hp"] > 0:
            dfs(new_state)


# Initial game state (Example - you'll need to adjust this)
initial_state = {
    "hp": 50,
    "mana": 500,
    "boss_hp": 58,
    "boss_damage": 9,
    "armor": 0,
    "effects": {},
    "mana_spent": 0
}

if __name__ == "__main__":
    dfs(initial_state)
    print("Minimum mana spent:", min_mana_spent)