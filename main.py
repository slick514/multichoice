import random

questions = []

class MultichoiceQuestion:
    def __init__(self, question):
        self._choices = {}
        self._question = question
        self._right_answer = ""
        self._wrong_answers = []

    def add_wrong_answer(self, wrong_answer):
        self._wrong_answers.append(wrong_answer)

    def set_right_answer(self, answer):
        self._right_answer = answer

    def prompt_user(self):
        self.print_question()
        self.print_choices()
        print("Your Answer: ")

    def print_question(self):
        print(self._question)

    def print_choices(self):
        self.create_choices()
        for key in sorted(self._choices.keys()):
            print(f'{key}: {self._choices[key]}')

    def test(self, answer)->bool:
        upper_ans = answer.upper()
        while upper_ans not in self._choices.keys():
            print(f'Invalid choice \'{upper_ans}\'\nPlease try again')
            self.prompt_user()
            answer = input()
            upper_ans = answer.upper()
        success_fail = self._choices[upper_ans] == self._right_answer
        print(f'Your choice was "{upper_ans}: {self._choices[upper_ans]}"')
        print("CORRECT" if success_fail else "INCORRECT")
        return success_fail

    def create_choices(self):
        self._choices.clear()
        random.shuffle(self._wrong_answers)
        num_choices = len(self._wrong_answers) + 1
        correct_index = random.randint(0, num_choices - 1)
        index = 0
        char_base = ord('A')
        if correct_index == 0:
            self._choices[chr(char_base + index)] = self._right_answer
            index += 1
        for answer in self._wrong_answers:
            self._choices[chr(char_base + index)] = answer
            index += 1
            if correct_index == index:
                self._choices[chr(char_base + index)] = self._right_answer
                index += 1

def q1()->MultichoiceQuestion:
    q = MultichoiceQuestion("What... is the capital of Assyria?")
    q.add_wrong_answer("Shubat-Enlil")
    q.add_wrong_answer("Kalhu")
    q.add_wrong_answer("Dur-Sharrukin")
    q.add_wrong_answer("Aššur")
    q.add_wrong_answer("Nineveh")
    q.add_wrong_answer("Harran")
    q.set_right_answer("I don't know that!")
    return q

def q2()->MultichoiceQuestion:
    q = MultichoiceQuestion("What... is the airspeed velocity of an unladen swallow?")
    q.add_wrong_answer("42")
    q.add_wrong_answer("Ni!")
    q.set_right_answer("What do you mean; an African or European swallow?")
    return q

def q3()->MultichoiceQuestion:
    q = MultichoiceQuestion("What also floats in water?")
    q.add_wrong_answer("Very small rocks")
    q.add_wrong_answer("Bread")
    q.add_wrong_answer("Apples")
    q.add_wrong_answer("Cider")
    q.add_wrong_answer("Churches")
    q.add_wrong_answer("Lead")
    q.add_wrong_answer("Grape gravy")
    q.add_wrong_answer("Cherries")
    q.add_wrong_answer("Mum")
    q.set_right_answer("A duck")
    return q

def q4()->MultichoiceQuestion:
    q = MultichoiceQuestion("What shall the number of the counting be?")
    q.add_wrong_answer("Two")
    q.add_wrong_answer("Four")
    q.add_wrong_answer("Five")
    q.set_right_answer("Three")
    return q

def q5()->MultichoiceQuestion:
    q = MultichoiceQuestion("What is Brian?")
    q.add_wrong_answer("The Messiah")
    q.add_wrong_answer("A Red Sea Pedestrian")
    q.add_wrong_answer("A Roman")
    q.set_right_answer("A very naughty boy")
    return q

def create_questions():
    questions.append(q1())
    questions.append(q2())
    questions.append(q3())
    questions.append(q4())
    questions.append(q5())

def run_quiz():
    create_questions()
    score = 0
    for question in questions:
        print()
        question.prompt_user()
        answer = input()
        score += question.test(answer)

    print(f'\nYour score is {score}')

if __name__ == "__main__":
    run_quiz()