import re
from itertools import combinations

# Shop items: (Cost, Damage, Armor)
weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0)
]

armors = [
    ("None", 0, 0, 0),  # Armor is optional
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5)
]

rings = [
    ("None1", 0, 0, 0),  # Rings are optional
    ("None2", 0, 0, 0),  # Allows choosing 0, 1, or 2 rings
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3)
]

def get_all_loadouts():
    """Generate all possible equipment loadouts."""
    for weapon in weapons:
        for armor in armors:
            for ring_combo in combinations(rings, 2):  # Choose 2 rings (or "None")
                yield [weapon, armor, *ring_combo]

def battle(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    """Simulate the battle between the player and the boss."""
    # Calculate damage dealt per turn (minimum 1)
    player_attack = max(1, player_damage - boss_armor)
    boss_attack = max(1, boss_damage - player_armor)

    # Compute number of turns to defeat opponent
    player_turns_to_win = (boss_hp + player_attack - 1) // player_attack
    boss_turns_to_win = (player_hp + boss_attack - 1) // boss_attack

    return player_turns_to_win <= boss_turns_to_win  # True if player wins


def readInput(fileName):
    min_cost = float("inf")
    max_cost = float("-inf")
    with open(fileName,"r") as file:
        lines = file.read().strip()
    bossHPDMGARM = re.findall(r"\d+",lines)
    bossHPDMGARM = [int(num) for num in bossHPDMGARM]
    BOSS_HP = bossHPDMGARM[0]
    BOSS_DAMAGE = bossHPDMGARM[1]
    BOSS_ARMOR = bossHPDMGARM[2]
    PLAYER_HP = 100


    for loadout in get_all_loadouts():
        total_cost = sum(item[1] for item in loadout)
        total_damage = sum(item[2] for item in loadout)
        total_armor = sum(item[3] for item in loadout)

        # Simulate battle
        if battle(PLAYER_HP, total_damage, total_armor, BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR):
            min_cost = min(min_cost, total_cost)  # Min gold spent to win
        else:
            max_cost = max(max_cost, total_cost)  # Max gold spent to lose

    return min_cost, max_cost


if __name__=='__main__':
    print(readInput("input.txt"))

