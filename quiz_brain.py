import html


class QuizBrain:
    def __init__(self, question_list):
        """initialize quiz mechanic variables"""
        self.question_number = 0
        self.question_list = question_list
        self.current_question = question_list[self.question_number]
        self.score = 0

    def still_has_questions(self) -> bool:
        """check for remaining questions"""
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """returns next question"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False)? ")
        # self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str) -> bool:
        """compares user answer to the current question answer"""
        # Pass the current question here too to get the answer
        current_question = self.current_question
        correct_answer = current_question.answer
        # print(f"You answered: {user_answer}, and it was actually {correct_answer}")
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
