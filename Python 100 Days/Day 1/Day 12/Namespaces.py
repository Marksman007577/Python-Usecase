# local vs global scope
#enemies = 1  # in the global scope


#def increase_enemies():
    #enemies = 2  # in the local scope
    #print(f"enemies inside function: {enemies}")

#increase_enemies()
#print(f"enemies inside function: {enemies}")


############# Local Scope ##################
#def drink_portion():
    #portion_strength = 2
    #print(portion_strength)


#drink_portion()
#print(portion_strength)

############# Global Scope ##################
player_health = 10


def drink_portion():
    global player_health
    portion_strength = 2
    print(portion_strength)
    print(player_health)


drink_portion()
