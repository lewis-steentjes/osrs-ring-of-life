## Script to run multiple simulations to identify the
## probability that a ring of life will save you in OSRS

## "if the wearer is dealt damage and has 10% or less of their Hitpoints 
## remaining. However, the ring is not foolproof, as a player wearing 
## one will still die if they are hit from above 10% of their maximum 
## Hitpoints to zero. " -OSRS Wiki {Ring of Life}

## We are assuming that the player does not eat or do anything to
## manipulate their HP and that the ring of life uses floor rounding
## to determine the player's required HP to activate.

import random

PLAYER_MAX_HP = 99 #set player HP
PLAYER_HP_TO_PROC = PLAYER_MAX_HP//10 #Activation HP
ENEMY_MAX_HIT = 8 #Set the max hit for the enemy you're facing
                   #Assuming one enemy attack style
                   
n = 100000 #number of lives to simulate
ringOfLifeSuccesses = 0 

for i in range(1, n+1):
    playerHP = PLAYER_MAX_HP
    while (playerHP > PLAYER_HP_TO_PROC): #cycle through combat until HP is low
        enemyHit = random.choice(range(0, ENEMY_MAX_HIT+1))
        playerHP = playerHP - enemyHit
        
    if (playerHP > 0):
        ringOfLifeSuccesses += 1


RoLSuccessRate = (float(ringOfLifeSuccesses)/(n))



## Display data
print("Player's Max HP: " + str(PLAYER_MAX_HP))
print("Enemy's Max Hit: " + str(ENEMY_MAX_HIT))



print("")
print("RoL Successes: " + str(ringOfLifeSuccesses))
print("Number of Attempts: " + str(n))
print("Overall Success Rate: " + str(RoLSuccessRate) )
















