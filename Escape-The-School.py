import random , sys , time , pickle
from rich.prompt import Prompt as p

def print_slow(str , t=0.05):
    t = 0.00000001
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(t)

def animation(string):
    print("\n", end="")
    for i in range(len(string)):
        print(" "*(i+1), end="\r")
        print("|"*(i+1) + string[i:], end="\r")
        time.sleep(0.1)

animation(' ||| Welcome! |||')

class Settings:
    
    Teacher = True
    Disresected = False
    Work = False
    Classroom_escape_attempts = 0

class Player:
    
    def __init__(self):
        
        self.level = 1
        self.health = 30
        self.damage = 10
        
        self.initial_health = self.health
        self.initial_damage = self.damage
        
        self.inventory = []
        self.items = ["Hall Pass" , "Key Card" , "Janitor's Keys" , "Main Keys"]

    def reset(self):
        
        self.health = self.initial_health
        self.damage = self.initial_damage
        
        print('\n')
        print_slow(f"Your health has been restored to {self.health} and, damage to {self.damage}")
        print('\n')

    def level_up(self):
        
        self.level += 1
        self.health += 20
        self.damage += 5
        
        print('\n')
        print_slow(f"You're now level {self.level}")
        print('\n')
    
    def pick_up_item(self, item):
        
        self.inventory.append(item)
        
        print('\n')
        print(f"You picked up a {item}")
        print('\n')

    def drop_item(self, item):
        
        self.inventory.remove(item)
        
        print('\n')
        print(f"You dropped the {item}")
        print('\n')

    def take_damage(self, damage):
        
        self.health -=float(damage)
        
        print('\n')
        print(f"You took {damage} damage, your health is now {round(self.health,1)}")
        print('\n')
        
class Game:
    
    def run(self):
    
        print('''\n
            1) Start game | 2) Skip to hallway | 3) load a game''')
        
        option = int(p.ask("[>] Select one"))
        
        if option == 1:
            self.eng_class()
        elif option == 2:
            self.hallway()
        elif option ==3:
            print(WIP)
            self.eng_class()

    
    def hallway(self):
        
        print('\n')
        print_slow("You're in the school hallway.\n", t=0.01)
        print('''\nWhat would you like to do?\n
              1) Go to Bathroom  | 2) Go to Janitor's Closet
              3) Talk To Teacher | 4) Go throught main door\n''')
        
        ans = int(p.ask('[>] Enter an Input: ',
                        choices=['1','2','3','4']))
        
        if ans == 1:
            self.bathroom()
        
        elif ans == 2:
            self.janitor_closet()
            
        elif ans == 3:
            self.talk()
            
        elif ans == 4:
            self.ask()

            
    def talk(self):
        if "Hall Pass" in player.inventory:
            
            if "Main Keys":
                print_slow("Thanks dawggg you can just leave by the front door now")
                ans  = p.ask('[>] Leave by front door?',
                      choices=['y','n'])
                if ans == 'y':
                    print(WIP)
                else:
                    print_slow('Okay then...? just stayy in the school i guess... Nerd')
                    self.hallway()
            
            else:
                print_slow("You ask for the way out, the teacher agrees to tell you if you help her get her purse from the janitor's closet.")
          
        else:
              
            print_slow("You attempt to talk you the teacher.\n")
            print_slow("Hold up.. Wheres you Hall Pass?\n" , t=0.0001)
            time.sleep(1)
            print_slow("The teacher takes you back to english class\n")
            time.sleep(3)
            self.eng_class()
            
    def janitor_closet(self):
        if "Janitor's Keys" in player.inventory:

            ans = p.ask('Do you wish to knock on the door?',
                        choices=["yes", "no"])
            
            if ans == "no":
                
                self.hallway()
                
            else:
                print('You guessed it..\n')
                print_slow('The door slowly opens to the janitors face', t= 0.1)
                
                animation('Janitor Fight') ; print_slow('||| Fight Initiated |||')
                enemy = Enemy()
                enemy.fight(name='Janitor')
                
            
        else:
            
            print_slow("lol you thought it would be that easy.. Its locked.")
            time.sleep(3)
            self.hallway()

    def bathroom(self):
        
        print('\n')
        print_slow('You walk into the bathroom and do your business\n')
        time.sleep(1)
        print_slow('You walk out and relise that your in the wrong bathroom...\n')
        time.sleep(1)
        print_slow('You slowly walk out...\n')
        time.sleep(2)
        print('\n')
        self.hallway()

    def eng_class(self):
        
        player = Player()
        settings = Settings()
        
        print('\n')
        print_slow("You're in English class.\n" , t=0.01)
        print('''\nWhat would you like to do?\n
              1) Wait | 2) Escape
              3) Work | 4) Ask the Teacher a question\n''')
        
        ans = int(p.ask('[>] Enter an Input: ',
                        choices=['1','2','3','4',]))
        
        if ans == 1:
            self.wait()
        
        elif ans == 2:
            self.escape()
            
        elif ans == 3:
            self.work()
            
        elif ans == 4:
            self.ask()
            

    def wait(self):
        
        print('\n')
        print_slow('You wait...\n' , t=0.1)
        time.sleep(1.5)
        print_slow('You wait even longer...\n' , t=0.2)
        time.sleep(2)
        print_slow("You're still waiting...\n" , t=0.3)
        time.sleep(3)
        if Settings.Teacher == True:
            print_slow("The bell goes.. but the teacher does'nt let you go...\n")
            game.eng_class()
        else:
            print_slow('The bell goes.. so you decide to escape\n')
            self.escape()
        
        print('\n')
        game.eng_class()
        
    def escape(self):
        
        if Settings.Teacher == True:
            
            if Settings.Classroom_escape_attempts == 0:
                print('\n')
                print_slow('The teacher caught you. You now have detention.')
                time.sleep(1)
                print('\n')
                Settings.Classroom_escape_attempts = Settings.Classroom_escape_attempts + 1
                
            elif Settings.Classroom_escape_attempts == 1:
                print('\n')
                print_slow('The teacher caught you again. Really? twice??')
                time.sleep(1)
                print('\n')
                Settings.Classroom_escape_attempts = Settings.Classroom_escape_attempts + 1
            
            elif Settings.Classroom_escape_attempts == 2:
                print('\n')
                print_slow('Okay.. if it didnt work the 1st 2 times why would it work now?')
                time.sleep(1)
                print('\n')
                Settings.Classroom_escape_attempts = Settings.Classroom_escape_attempts + 1
            
            elif Settings.Classroom_escape_attempts == 3:
                print('\n')
                print_slow('Why am i still programming more...?')
                time.sleep(1)
                print('\n')
                Settings.Classroom_escape_attempts = Settings.Classroom_escape_attempts + 1
            
            elif Settings.Classroom_escape_attempts == 4:
                print('\n')
                print_slow('Nope.')
                time.sleep(1)
                print('\n')
                Settings.Classroom_escape_attempts = Settings.Classroom_escape_attempts + 1
                
            elif Settings.Classroom_escape_attempts > 4:
                print('\n')
                print_slow(f'The developer personally slaps you after trying to escape {Settings.Classroom_escape_attempts + 1} times..')
                time.sleep(1)
                print('\n')
                Settings.Classroom_escape_attempts = Settings.Classroom_escape_attempts + 1
                
            self.eng_class()
            
        else:
            
            print('\n')
            print_slow('You have escaped to the hallway.')
            time.sleep(1)
            self.hallway()
            print('\n')
            
    def work(self):
        
        if Settings.Work == False:
        
            print('\n')
            print_slow("You do you'r work..\n")
            time.sleep(1)
            print_slow("You are close to finishing..\n")
            time.sleep(1)
            print_slow("Final question... \n")
            
            time.sleep(.5)
            
            print('''What is a noun?\n
                    1) A word to describe an object / thing \n
                    2) A word to identify an object / thing \n
                    3) A word to describe an action\n''')
            
            ans = int(p.ask('[>] Select an input' , 
                        choices=['1','2','3']))
            
            if ans == 2:
                
                print('\n')
                print_slow("Correct,  you got awarded with a Hall Pass \n")
                time.sleep(1)
                player.pick_up_item("Hall Pass")
                Settings.Work = True
                print('\n')
                self.eng_class()
                
            else:
                
                print('\n')
                print_slow("Incorrect, you should be disapaionted in yourself.")
                time.sleep(1)
                print('\n')
                self.eng_class()
                
        else:
            
            print('\n')
            print_slow('You already did your work... Nerd')
            time.sleep(1)
            print('\n')
            self.eng_class()
            
    def ask(self):
        
        if Settings.Teacher == True:
        
            print('\n')
            print('''What do you want to ask the teacher?\n
                1) Can I use the bathroom?
                2) Insult the teacher
                3) When is the bell?''')
            print('\n')
            
            ans = int(p.ask('[>] Select an option',
                            choices=['1','2','3']))
            
            if ans == 1:
                print('\n')
                print_slow("I don't know, caaaaannnn yooouuu???")
                print('\n')
                p.ask('[>] Rephrase the sentence',
                                choices=['May I use the bathroom please?'])
                print('\n')
                print_slow("Hahahaha lol, no (personally i would'nt accept this level of disrespect)")
                print('\n')
                Settings.Disresected = True
                game.eng_class()
                
            elif ans == 2:
                print('\n')
                print_slow("You ask the teacher how much they get paid...\n")
                time.sleep(2)
                print_slow('Teacher didnt like that.\n' ,t=0.3)
                time.sleep(4)
                
                if Settings.Disresected == True:
                    print_slow('The teacher has discrspected me before.. time to pay..')
                    print('\n')
                    time.sleep(2)
                
                animation('TEACHER FIGHT!')
                print_slow('||| Fight Initiated |||')
                print('\n')
                
                time.sleep(2)
                
                enemy = Enemy()
                enemy.fight(name='Teacher')
                print('\n')
                
            elif ans == 3:
                print('\n')
                print_slow('When I want lololol hahahaha')
                Settings.Disresected = True
                print('\n')
                game.eng_class()
                
        else: print_slow('The teacher isnt present anymore...... huh, i wonder why.') ; self.eng_class()
                    
class Enemy:
    def __init__(self):
        self.enemies = {"Teacher": {"health": 35, "damage": 15, "insult_multiplier": round(random.uniform(1.1,2) , 1)}, 
                        "Janitor": {"health": 60, "damage": 20,"insult_multiplier": random.randint(2,3)},
                        "Dragon": {"health": 100, "damage": 30, "insult_multiplier":random.randint(2,4)}}
    
    def fight(self,name):
        
        if name in self.enemies:
            
            enemy = self.enemies[name]
            enemy_health = enemy["health"]
            enemy_damage = enemy["damage"]
            insult_multiplier = enemy["insult_multiplier"]
             
            while player.health > 0 and enemy_health > 0:
                
                print(f'''
                      Your Health: {round(float(player.health),1)}\n
                      Your Damage: {round(float(player.damage),1)}\n
                      ----------------\n
                      Enemy Health: {round(float(enemy_health),1)}\n
                      Enemy Damage: {round(float(enemy_damage),1)}\n''')
                
                print("What do you want to do?\n1) Attack\n2) Defend\n3) Insult\n4) Apologise\n")
                choice = input('[>] Enter an option: ')
                print('\n')
                
                if choice == "1":
                    enemy_health -= round((float(player.damage)) , 1)
                    print_slow(f"You attacked the {name} and dealt {player.damage} damage. {name}'s health is now {enemy_health}\n")
                    
                elif choice == "2":
                    enemy_damage = round(random.uniform(enemy_damage/2, enemy_damage), 1)
                    print_slow(f"You defended and reduced the {name}'s damage. {name}'s damage is now {enemy_damage}\n")

                    
                elif choice == "3":
                    player.damage = player.damage * insult_multiplier
                    print_slow(f"You insulted the {name} and increased your damage by {insult_multiplier}. Your damage is now {player.damage}\n")
                    
                elif choice == "4":
                    
                    print_slow("Don't worry you just didn't want the smoke")
                    player.reset()
                    
                    game.eng_class()
                    break
                    
                else:
                    print_slow("Invalid choice\n")
                    
                    
                weights = [2, 1, 1]
                choices = [1, 2, 3]

                if (enemy_damage) <= 0:
                    enemy_damage = 2
                    enemy_choice == 3
                else:
                    enemy_choice = random.choices(choices, weights)[0]

                
                if enemy_choice == 2:
                    
                    player.damage = round(random.uniform(player.damage/2, player.damage), 1)
                    print_slow(f"{name} defended and reduced you'r damage. Your damage is now {player.damage}\n")
                
                elif enemy_choice == 3:
                    
                    enemy_damage = round(enemy_damage, 1) * round(insult_multiplier , 1)
                    print_slow(f"{name} insulted you and increased its damage damage. {name}'s damage is now {enemy_damage}\n")
                    
                if enemy_health > 0:
                    if enemy_choice == 1:
                        print_slow(f"{name} attacked you and dealt {round(enemy_damage,1)} damage.\n")
                        player.take_damage(enemy_damage)
                    
                if enemy_health <= 0:
                    
                    print("You defeated the enemy!\n")
                    
                    if name == 'Teacher':
                        player.pick_up_item("Key Card")
                        Settings.Teacher = False
                    elif name == 'Janitor':
                        player.pick_up_item("Janitor's Keys")
                    
                    player.reset()
                    player.level_up()
                    player.reset()
                    
                    print("\n")
                    
                    game.eng_class()
                    
                if player.health <= 0:
                    print('\n')
                    print_slow("You have been defeated\n")
                    Settings.Disresected = True
                    player.reset()
                    game.eng_class()
                    
                
                    
        else: print('enemy not found')


        
player = Player()
game = Game()

game.run()
