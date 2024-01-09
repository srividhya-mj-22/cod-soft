class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0

    def display_question(self):
        question = self.questions[self.current_question]['question']
        options = self.questions[self.current_question]['options']
        print(f"Question {self.current_question + 1}: {question}")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

    def check_answer(self, answer):
        correct_answer = self.questions[self.current_question]['answer']
        if answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{len(self.questions)}")
        self.current_question += 1

    def start_quiz(self):
        while self.current_question < len(self.questions):
            self.display_question()
            user_answer = input("Enter your choice (1, 2, 3, 4,etc.): ")
            self.check_answer(user_answer)
        print("You Are Done with all the Questions!")
        print(f"You scored : {self.score}/{len(self.questions)}")



questions = [
    {
        'question': 'What is the capital of India?',
        'options': ['Mumbai', 'Hyderabad', 'Delhi', 'Banglore'],
        'answer': '3'
    },
    {
        'question': 'Who is known as Iron Lady of India?',
        'options': ['Kiran Bedi', 'Draupadhi murmu', 'Nirmala sitaraman', 'Indira Gandhi'],
        'answer': '4'
    },

]


my_quiz = Quiz(questions)
my_quiz.start_quiz()
