from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
from random import randint
from time import sleep

class Game:
    def __init__(self):
        self.kb = KBHit()
                
    def play_life(self):
        start_cue = input("Type R to Begin the Game of Life: ")
        match start_cue:
            case "R" | "r":
                while True:
                    self.begin_life()
                    again = input("Start a New Colony?\nY/N\n")
                    match again:
                        case "y"|"Y"|"yes"|"YES"|"Yes":
                            pass
                        case "n"|"N"|"NO"|"No"|"no":
                            print("Thank You for Playing")
                            break
            case _:
                print("Only random seeding is available, please type 'r' next time")


    def begin_life(self):
        self.generation = 0
        self.end=False
        self.quit=False
        rows= randint(10, 20)
        cols= randint(10, 20)
        self.colony = Grid(rows, cols)
        self.colony.first_generation()
        print(f"Generation 0:\n{str(self.colony)}\nPress 'q' to quit\nPress 's' to move to next generation\nPress 'a' to automatically progress\n")
        while self.end == False and self.quit==False:
            if self.kb.kbhit():
                c = (self.kb.getch())
                c_ord = ord(c)
                if c_ord == 115:
                    self.manual_mode()
                elif c_ord == 113:
                    self.quit=True
                    break
                elif c_ord == 97:
                    self.auto_mode()
        if self.end == True:
            print(f"Colony ended due to non-stability.\nColony persisted for {self.generation} generations.")
        elif self.quit == True:
            print(f"Colony ended due to player input.\nColony persisted for {self.generation} generations.")
                            
            
    
    def manual_mode(self):
            self.colony.generate_next_grid()
            self.generation +=1
            print(f"Generation {self.generation}:\n{str(self.colony)}\n")
            if self.colony.repeating_grids():
                self.end = True
            
            
    
    def auto_mode(self):
        print("Auto-Progression enabled\nPress 'm' to switch to Manual Progression\n")
        while True:
            sleep(1)
            self.colony.generate_next_grid()
            self.generation +=1
            print(f"Generation {self.generation}:\n{str(self.colony)}\n")
            if self.kb.kbhit():
                c = (self.kb.getch())
                c_ord = ord(c)
                if c_ord == 109:
                    print("Manual Progression enabled\nPress 'a' to switch to Auto-Progression\n")
                    break
                if c_ord == 113:
                    self.quit=True
                    break
            if self.colony.repeating_grids():
                self.end = True
                break
                

