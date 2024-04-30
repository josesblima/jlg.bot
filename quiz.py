from tobira import Tobira
class Quiz:
    def __init__(self):
        self.active_quiz = None
    def quiz_starter(self, message):
        p_message = message.content.lower()
        if (p_message == 'tobira'):
            self.active_quiz = Tobira()
            print("quiz_starter\n")
            return self.active_quiz.get_new_question()

    def quiz_handler(self, message):
        p_message = message.content.lower()
        if self.active_quiz.check_answer(message) == True:
            return self.active_quiz.get_new_question()
        return
