# Enter combat or enter shop
# Entering combat spawns a random enemy
# Combat options: Attack enemy, use item, pass, flee
# Get coins on victory
# Entering shop populates the inventory with 3 random items
# Shop options: Purchase item 1, 2, or 3, exit
# 
import random
#CLASSES

#ITEM CLASSES
class Item():
    def __init__(self):
        self.durability = 1
        self.name = 'Item'
        self.cost = 10

    def Use(self, user):
        if(self.durability > 0):
            self.durability -= 1

class HealthPotion(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Health Potion'
        self.healthRestore = 10
        self.cost = 10

    def Use(self, user):
        if(self.durability > 0):
            user.health += self.healthRestore
            print("Restored " + str(self.healthRestore) + " to " + user.name)
            self.durability -= 1
        if(self.durability <= 0):
            print("%s is empty" % self.name)

class Shield(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Shield'
        self.cost = 20
        self.armorValue = 2

    def Use(self, user):
        if(self.durability > 0):
            user.armor += self.armorValue
            print(user.name + "Equipped a shield, adding " + str(self.armorValue) + " armor.")
            self.durability -= 1
        if(self.durability <= 0):
            print("%s is broken" % self.name)

class TheOneRing(Item):
    def __init__(self):
        super().__init__()
        self.name = 'The One Ring'
        self.cost = 100
        self.dodgeChanceValue = 10

    def Use(self, user):
        if(self.durability > 0):
            user.dodgeChance += self.dodgeChanceValue
            print(user.name + "Equipped The One Ring, adding " + str(self.dodgeChanceValue) + "% Dodge Chance.")
            self.durability -= 1
        if(self.durability <= 0):
            print("%s's power is spent" % self.name)

#CHARACTER CLASSES
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
        # self.healthPot = HealthPotion()
        # self.shield = Shield()
        # self.oneRing = TheOneRing()
        self.inventory = []
        self.armor = 0
        self.dodgeChance = 0
        

    def attack(self, target):
        target.health -= self.power
        print("%s deals %d damage to %s." % (self.name,self.power, target.name))
        if target.health <= 0:
            print("%s is dead." % target.name)
        
    def isAlive(self):
        if(self.health > 0):
            return True
        else:
            return False

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
    
    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print(item.name + " has a durability of " + str(item.durability))
    
    def addToInventory(self, item):
        self.inventory.append(item)

    def takeDamage(self, damage):
        dodgeRoll = random.randrange(1, 100)
        if(dodgeRoll >= self.dodgeChance):
            self.health -= (damage - self.armor)
        else:
            print(self.name + "dodged the attack")  

class Hero(Character):
    def __init__(self, health, power, name):
        super(Hero,self).__init__(health, power, name)
        self.critChance = 2
        self.gold = 100

class Enemy(Character):
    def __init__(self, health, power, name, goldDropAmount):
        super(Enemy,self).__init__(health, power, name)
        self.goldDropAmount = goldDropAmount

class Medic(Enemy):
    def __init__(self, health, power, name, goldDropAmount):
        super(Medic, self).__init__(health, power, name, goldDropAmount)
        self.goldDropAmount = 7
    
    def takeDamage(self, damage):
        self.health -= damage
        healRoll = random.randrange(1,10)
        if(healRoll <= 2):
            self.health += 2
            print(self.name + " healed for 2" )

class Shadow(Enemy):
    def __init__(self, health, power, name, goldDropAmount):
        super(Shadow, self).__init__(health, power, name, goldDropAmount)
        self.dodgeChance = 10

class Zombie(Enemy):
    def __init__(self, health, power, name, goldDropAmount):
        super(Zombie, self).__init__(health, power, name, goldDropAmount)
    
    def isAlive(self):
        return True

#VARIABLES
gandalf = Hero(10,10, 'Gandalf')
inShop = False

#GLOBAL FUNCTIONS
def print_start():
        print()
        print("What do you want to do?")
        print("1. Fight Enemy")
        print("2. Enter Shop")
        print("3. Check Inventory")
        print("4. Quit")
        print("> ",)

def shop(hero):
    print("Welcome to the shop, you have " + str(gandalf.gold) + " Gold")
    inShop = True
    shopInventory = generateShopInventory()
    while inShop == True:
        print_divider()
        printShopInventory(shopInventory)
        print("> ",)
        user_input = input()
        if user_input == "1":
            print("Purchasing Item 1!")
            purchaseItem(hero, shopInventory[int(user_input) - 1], shopInventory)
        elif user_input == "2":
            print("Purchasing Item 2!")
            purchaseItem(hero, shopInventory[int(user_input) - 1], shopInventory)
        elif user_input == "3":
            print("Purchasing Item 3!")
            purchaseItem(hero, shopInventory[int(user_input) - 1], shopInventory)
        elif user_input == "4":
            print("Exiting Shop")
            inShop = False
        else:
            print("Invalid input %r" % user_input)

def combat(hero, enemy):
    print("%s has appeared to fight!" % enemy.name)
    print_divider()
    while hero.isAlive() and enemy.isAlive():
        hero.print_status()
        enemy.print_status()
        print_divider()
        print("What do you want to do?")
        print("1. Attack Enemy")
        print("2. Use Item")
        print("3. Do Nothing")
        print("4. Flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks Enemy
            critRoll = random.randrange(1,10)
            attackDamage = hero.power
            if(critRoll <= hero.critChance):
                print("CRITICAL HIT!")
                attackDamage = hero.power*2
            enemy.takeDamage(attackDamage)
            print("You do %d damage to %s." % (attackDamage, enemy.name))
            if enemy.isAlive() == False:
                hero.gold += enemy.goldDropAmount
                print("The enemy is dead and the hero loots %d Gold" % enemy.goldDropAmount)
        elif user_input == "2":
                print_divider()
                print("Choose an item: ")
                #hero.print_inventory()
                inventoryCounter = 1
                for item in hero.inventory:
                    print("%d. %s" % (inventoryCounter, item.name))
                    inventoryCounter += 1
                user_input = input()
                hero.inventory[int(user_input) - 1].Use(hero)
        elif user_input == "3":
            pass
        elif user_input == "4":
            print_divider()
            print("You have fled combat")
            break
        else:
            print_divider()
            print("Invalid input %r" % user_input)

        if enemy.isAlive() == True:
            # enemy attacks hero
            hero.takeDamage(enemy.power)
            print("%s does %d damage to you." % (enemy.name, enemy.power))
            if hero.isAlive() == False:
                print("You are dead.")

def generateEnemy():
    enemyChoice = random.randrange(1,4)
    goldAmount = random.randrange(1,10)
    if(enemyChoice == 1):
        goldAmount = random.randrange(1,10)
        myEnemy = Enemy(6,2, 'Balrog',goldAmount)
    if(enemyChoice == 2):
        goldAmount = random.randrange(1,3)
        myEnemy = Zombie(2,2,'Sauron',goldAmount)
    if(enemyChoice == 3):
        goldAmount = random.randrange(1,6)
        myEnemy = Medic(2,5,'Witch King',goldAmount)
    if(enemyChoice == 4):
        goldAmount = random.randrange(1,8)
        myEnemy = Shadow(1,10,'Gollum',goldAmount)
    return myEnemy

def generateRandomShopItem(itemList):
    itemRoll = random.randrange(1,3)
    if(itemRoll == 1):
       itemList.append(HealthPotion())
    if(itemRoll == 2):
        itemList.append(Shield())
    if(itemRoll == 3):
        itemList.append(TheOneRing())
    # if(itemRoll == 4):
    #     generatedInventory.append(HealthPotion())
    # if(itemRoll == 5):
    #     generatedInventory.append(HealthPotion())

def generateShopInventory():
    generatedInventory = []
    print("Generating Inventory")
    generateRandomShopItem(generatedInventory)
    generateRandomShopItem(generatedInventory)
    generateRandomShopItem(generatedInventory)
    return generatedInventory

def printShopInventory(shopInventory):
    shopCounter = 1
    for item in shopInventory:
        print("%d. %s" % (shopCounter, item.name))
        shopCounter += 1
    print("4. Exit Shop")

def purchaseItem(hero, item, shopInventory):
    if(hero.gold >= item.cost):
        hero.inventory.append(item)
        shopInventory.remove(item)
        hero.gold -= item.cost

def print_divider():
    print("--------------------------------")

def main():
    while gandalf.isAlive():
        print_start()
        user_input = input()
        if user_input == "1":
            #hero attacks enemy
            #gandalf.attack(sauron)
            print("Entering Combat!")
            combat(gandalf, generateEnemy())
        elif user_input == "2":
            print("Entering Shop!")
            inShop = True
            shop(gandalf)
        elif user_input == "3":
            print("Checking Inventory!")
            gandalf.print_inventory()
        elif user_input == "4":
            print("Quitting game.")
            break
        else:
            print("Invalid input %r" % user_input)


#MAIN
main()