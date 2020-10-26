# Calculus Trivia Game 

from subprocess import call 
import os 

class Question: 
    def __init__(self, category, prompt, answer): 
        self.category = ["Functions", "Derivatives", "Integrals"]
        self.prompt = prompt
        self.answer = answer 
        self.on_question = 0

prompt_functions = [
    "Given function f(x) = x^2 + 6x - 11, find f(2). \n(a) 5 \n(b) 3 \n(c) -1 \n\n", 
    "Given the function f(x) = x^2, which statement is not true? \n(a) The function is quadratic. \n(b) The function is linear. \n(c) The function forms a curved parabola.\n\n",
    "Given function f(x) = 6x + 3, what is the slope? \n(a) 2 \n(b) 3 \n(c) 6 \n\n"
]

prompt_derivatives = [
    "Given f(x) = 2x^2 - 16x + 20, find the derivative. \n(a) f(x) = 2x^2 - 16 \n(b) f(x) = 2x - 16 \n(c) f(x) = 4x - 16 \n\n", 
    "Which rule would be used to find the derivative of f(x) = x / (x^2 + 5 )? \n(a) Product Rule \n(b) Quotient Rule \n(c) Chain Rule.\n\n",
    "A derivative is the _______ of the tangent line to the graph of f(x). \n(a) function \n(b) limit \n(c) slope \n\n"
]

prompt_integrals = [
    "Integration can be used to find the _______ between a function and the x-axis. \n(a) area \n(b) volume \n(c) limit \n\n", 
    "An indefinite integral is also known as: \n(a) no other term \n(b) antiderivative \n(c) summation \n\n",
    "A definite integral has limits defined on the:\n(a) y - axis \n(b) neither \n(c) x - axis\n\n"
]

quest_functions = [
    Question("Functions", prompt_functions[0], "a"), 
    Question("Functions", prompt_functions[1], "b"),
    Question("Functions", prompt_functions[2], "c")
]
quest_derivatives = [
    Question("Derivatives", prompt_derivatives[0], "c"), 
    Question("Derivatives", prompt_derivatives[1], "b"),
    Question("Derivatives", prompt_derivatives[2], "a")
]
quest_integrals = [
    Question("Integrals", prompt_integrals[0], "a"), 
    Question("Integrals", prompt_integrals[1], "b"),
    Question("Integrals", prompt_integrals[2], "c")
]
# def clear(): 
#     call('clear' if os.name == 'posix' else 'cls')

# playing = True
# while playing: 
#     clear()

def run_quiz():
    playing = True
    while playing: 
        try: 
            choice = int(input('''
***** Welcome to Calculus Trivia! ***** 

Please choose a category to review: 
(1) Functions 
(2) Derivatives 
(3) Integrals 
(0) Quit 
                '''))
            if choice == 0: 
                playing = False 
                break 
            elif choice > 3: 
                print("Invalid choice. Please pick category 1, 2, or 3.")
            
        except ValueError: 
            print("Invalid choice. Please pick category 1, 2, or 3.")

        score = 0 
        if choice == 1: 
            for question in quest_functions: 
                answer = input(question.prompt)
                if answer == question.answer:
                    score += 1 
            print("You got " + str(score) + "/" + str(len(quest_functions)) + "correct!") 

        elif choice == 2: 
            for question in quest_derivatives: 
                answer = input(question.prompt)
                if answer == question.answer:
                    score += 1 
            print("You got " + str(score) + "/" + str(len(quest_derivatives)) + "correct!") 

        elif choice == 3:   
            for question in quest_integrals: 
                answer = input(question.prompt) 
                if answer == question.answer: 
                    score += 1 
            print("You got " + str(score) + "/" + str(len(quest_integrals)) + "correct!") 

run_quiz()

# improvement: add class game + list of lists 
