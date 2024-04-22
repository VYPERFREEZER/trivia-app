#create a trivia app
#ask random questions, not necessarily
#provide answers and questions
#end game when user gets a question wrong
import sys

class Game:
    #questions and answers hash map
    questions ={
        1:{
            "question" : "What color are ripe apples? \nRed\nBlue\nGreen\n==> ",
            "answer" : "red"
        },
        2:{
        "question": "What color are unripe mangoes?\nRed\nGreen\nPurple\n==>",
        "answer": "green"
        },
        3:{
           "question": "What color are ripe bananas?\nMagenta\nOrange\nYellow\n==>",
           "answer": "yellow"
        }
    }
   
    
    #initialise points
    points = 0
    
    #initialise the class methods
    def __init__(self):
        pass
    
    #intro message and get user continue playing input
    def intro(self):
        accept = input("TRIVIA GAME\nPress \"q\" to quit game\nYou get asked random questions.\nYou get any of them wrong the game ends instantly!!\nDo you want to continue(yes(y) or no(n): ")
        return accept
    
    #ask_questions
    def ask_questions(self):
        for question in self.questions:
            response = input(self.questions[question]["question"]).lower()
            #check answer
            if response == self.questions[question]["answer"]:
                self.points += 1
                print("...+ 1")
            elif response == "q":
                self.quit_game()
                
            else:
                print("Incorrect!!")
                self.quit_game()
                
        self.quit_game()
                
    #end game
    def quit_game(self):
        print("=="*20)
        if self.points == 3:
            print("Hooray!! YOu Won")
        else:
            print("You Lost!!")
        print("Game Over")
        print(f"Total Points: {self.points}")
        
        sys.exit()
        
    #start game
    def start_game(self):
        accept = self.intro()
        while  accept not in ["y", "n", "q"]:
            print("**"*20)
            print("Invalid Input")
            accept = self.intro()
            continue
            
            
        if accept == "y":
                self.ask_questions()
        else:
            self.quit_game()    
        
            
game = Game()
game.start_game()

