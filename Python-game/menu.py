class Game: 
    def __init__(self, name, category, questions): 
        self.category = ["Derivatives", "Integers", "Functions", "Limits"]
        self.questions = 0
        self.name = name

    def ask_next_question(self):
        current_quest = self.questions[self.current_quest]
        print(current_quest["Problem":])

        # numbers options as they print 
        for indx, answer in enumerate(current_quest["Options"]):
            print(indx,answer)
        result = input("Pick a category:\n") 
        self.on_question += 1

    def run_quiz(self):
        print(f"Welcome to {self.name}")
        while self.on_question < len(self.questions):
            self.ask_next_question()

-----------

def ask_one_question(question):
    print("\n" + question)
    choice = input("Enter Your Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Enter again")
            choice = input("Enter Choice [a/b/c/d]: ")

def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.{0} Absolutely Correct!\n".format(key))
        return 2
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Right Answer is ({0})".format(actual))
        print ("Learn more : " + meta["more_info"] + "\n")
        return -1


def test(questions):
    score = 0
    print("General Instructions:\n1. Please enter only the choice letter corresponding to the correct answer.\n2. Each question carries 2 points\n3. Wrong answer leads to -1 marks per question\nQuiz will start momentarily. Good Luck!\n")
    time.sleep(10)
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    print("\n***************** RESULT ********************\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print("Your Score:", score, "/", (2 * len(questions)))

def load_question(filename):
    """
    loads the questions from the JSON file into a Python dictionary and returns it
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)


def play_quiz():
    flag = False
    try:
        choice = int(input("Welcome to Today's Quiz!\nChoose your domain of interest:\n(1). Science\n(2). History of India\n(3). Commerce\n(4). Technology\n(5). World Gk\nEnter Your Choice [1/2/3/4/5]: "))
        if choice > len(TOPICS_LIST) or choice < 1:
            print("Invalid Choice. Enter Again")
            flag = True # raising flag
    except ValueError as e:
        print("Invalid Choice. Enter Again")
        flag = True # raising a flag

    if not flag:
        questions = load_question('topics/'+TOPICS_LIST[choice-1]+'.json')
        test(questions)
    else:
        play_quiz() # replay if flag was raised