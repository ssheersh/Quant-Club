import random
import requests

class Wordle:
    def __init__(self):
        self.words = []
        response = requests.get('https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt')
        data = response.text
        lines = data.split('\n')
        for line in lines:
            self.words.append(line)     

        self.WORD = random.choice(self.words)   
        self.guesses = []
        self.feedbacks = [] 

    def feedback(self, guessword):
        feedback = []
        for i,letter in enumerate(guessword):
            if letter not in self.WORD:
                feedback.append(0)
            else:
                if letter == self.WORD[i]:
                    feedback.append(1)
                else:
                    feedback.append(2)
        
        return feedback
    
    def generate_guess(self, feedback = None):
        raise NotImplementedError("Implement the generate_guess() function first.")
        return ""

    def run(self):
        feedback = None
        flag = False
        for i in range(10):
            guessword = self.generate_guess(feedback)
            feedback = self.feedback(guessword)
            self.feedbacks.append(feedback)
            self.guesses.append(guessword)

            print("\tGuess #", i+1, "\t:", guessword, "\tFeedback: ", feedback)

            if guessword == self.WORD:
                flag = True
                print("\t\nSuccess.\tCorrect word: ",guessword, "\tNumber of guesses: ", len(self.feedbacks))
                break
        
        if not flag:
            print("\tFailed to find correct word within 10 guesses. \t Correct word: ", self.WORD)
        
        print('\n')


class Game:
    def __init__(self, Solver, N=10):
        self.Solver = Solver
        self.N = N
    
    def run(self):
        print("Simulating for ", self.N, " words.\n")
        for i in range(self.N):
            solver = self.Solver()
            print("WORD #[", i+1, "/", self.N, "]")
            solver.run()






