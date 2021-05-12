#CLASSES
class Character:
    def __init__(self, health, power, name):
        super.__init__(self, health, power, name)

    def attack(self, target):
        target.health -= self.power
        print("%s deals %d damage to %s." % (self.name,self.power, target.name))
        if target.health <= 0:
            print("%s is dead." % target.name)
        
    def isAlive(self):
        if(self.health >= 0):
            return True
        else:
            return False

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

class Enemy(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

class Zombie(Enemy):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    
    def isAlive(self):
        return True

#VARIABLES
gandalf = Hero(10,10, 'Gandalf')
balrog = Enemy(6,2, 'Balrog')
sauron = Zombie(2,2,'Sauron')

#GLOBAL FUNCTIONS
def print_start():
        gandalf.print_status()
        balrog.print_status()
        sauron.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)

def main():
    while sauron.isAlive() and gandalf.isAlive():
        print_start()
        user_input = input()
        if user_input == "1":
            #hero attacks enemy
            gandalf.attack(sauron)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Quitting game.")
            break
        else:
            print("Invalid input %r" % user_input)

        if sauron.health > 0:
            # enemy attacks hero
            sauron.attack(gandalf)

#MAIN
main()