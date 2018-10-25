#Gabriel Harrison
#10/12/18
import random
#Testing stuff
#day = "monday"



#Loops


##
##loops=0
##while True:
##    print("I have looped",loops,"times")
##    loops +=1
##    if loops==1000:
##        break

##count=0
##while True:
##    count+= 1
##    if count>100:
##        break
##    if count== 5 or count== 25 or count== 50:
##        continue
##    print(count)
##    
##input("\n\n press enter to exit")


##i="enter"
##while i == "enter":
##    print("Looping")
##    x=input("Do you want to keep looping yes or no?")
##    if x == "yes":
##        continue
##    else:
##        print(i)



##print("Your lone hero is surrounded by a massive army of trolls.")
##print("Their decaying green bodies stretch out, melting into the horizon.")
##print("Your hero unsheathes his sword for the last fight of his life.\n")
##
##
##health=10
##trolls=0
##damage=3
##
##while health !=0:
##    trolls+= 1
##    health-=damage
##    print("Your hero swings and defeats an evil troll,"\
##          "but takes",damage,"damage points.\n")
##    
##print("your hero ought valiantly and defeated", trolls,"trolls.")
##print("but alas, your hero is no more.")
##input("\n\nPress the enter key to exit.")
win=0      
monster_health= 100
player_health= 100
print("you are at 100 health", "and so is the monster")
choice =input("attack or run")



while choice=="attack":
    print("your attack the monster")
    player_damage=random.randrange(0,25)
    monster_damage=random.randrange(0,50)
    monster_health-= player_damage
    if monster_health>0:
        print("monster attacks you for", monster_damage)
        player_health -= monster_damage
    if player_health<=0:
        win=0
        print("You died")
        break
    elif monster_health<=0:
        win= 1
        print("you have killed the monster")
        break
    elif player_health >=0 and monster_health>=0:
        print("you have",player_health,"health")
        print("the monster has", monster_health, "health")
        choice=input("attack or run")
        if choice!= "attack" or choice !="run":
            print("I'm not sure what that was")
            choice="attack"
            continue
        else:
            continue

if choice=="run":
    print("you are a coward")


if win==0:
    print("game over")
else:
    print("you win")













    
