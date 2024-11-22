import random
#defining creatures/human attributes
playerSkill = 5
playerHealth = 30
playerLuck = 5

creatureSkill = 5
creatureHealth = 50

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def test_luck(luck):
    roll = roll_dice()
    return roll >= luck

while creatureHealth and playerHealth > 0:
    print("\n ----New Round----")
    # rolling for player and creature attack strenght
    creatureAttackStrength =  roll_dice() + creatureSkill
    print(f"Creatures attack strength : {creatureAttackStrength}")

    playerAttackStrength = roll_dice() + playerSkill
    print(f"Player attack strength : {playerAttackStrength}")
    #Now we minus the attack strength to the health of monster first and then player
    player_skill_double = playerAttackStrength * 2
    if playerAttackStrength > creatureAttackStrength:
        print("Player has hit creature")
        use_luck = input("Do you want to use 'luck' to deal extra damage? (yes/no)")
        if use_luck == "yes" and playerLuck > 0:
            if test_luck(playerLuck):
                print(f"You dealt {player_skill_double} damage, instead of {playerAttackStrength}")
                creatureHealth -= player_skill_double
            else:
                print(f"Luck failed you only did {playerAttackStrength}")
                creatureHealth -= playerAttackStrength
            playerLuck -= 1
        else:
            creatureHealth -= playerAttackStrength
    elif playerAttackStrength < creatureAttackStrength:
        CAS_half = creatureAttackStrength //2
        CAS_double = creatureAttackStrength * 2
        print("creature hits player")
        use_luck = input("you want to use luck to avoid extra damage? (y/n)")
        if use_luck == "y" and playerLuck > 0:
            if test_luck(playerLuck) == True:
                print(f"Luck succeeded! you take {CAS_half}, instead of {creatureAttackStrength}")
                playerHealth -= CAS_half
            else:
                print(f"you take {CAS_double}, instead of {creatureAttackStrength}")
                playerHealth -= CAS_double
        else:
            print("player did not use luck")
            playerHealth -= creatureAttackStrength
            print(f"player took {creatureAttackStrength} damage")
    else:
        print("both attacks missed")
    print(f"player health: {playerHealth}, player luck: {playerLuck}")
    print(f"create health: {creatureHealth}")

while creatureHealth > 0 and playerHealth > 0:
    print("\n The winner is player")
else:
    print("\nplayer has lost")





















