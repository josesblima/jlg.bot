from tobira import Tobira
import time

class Quiz:
    def __init__(self):
        self.active_quiz = None
        self.timer_sleep = False
        self.correct_answer_users_set = set()
        self.correct_answer_users_str = ""
    def quiz_starter(self, message):
        p_message = message.content.lower()
        if (p_message == 'tobira'):
            self.active_quiz = Tobira()
            print("quiz_starter\n")
            return self.active_quiz.get_new_question()

    def quiz_handler(self, message):
        p_message = message.content.lower()
        if self.active_quiz.check_answer(message) == True:
            if self.timer_sleep != True:
                print("sleep starts here")
                self.correct_answer_users_str = ""
                self.correct_answer_users_set.add(str(message.author.name))
                print(message.author)
                self.timer_sleep == True
                time.sleep(1)
                self.timer_sleep == False
                print("this is after tyhe sleep")
                for x in self.correct_answer_users_set:
                    print(x)
                    self.correct_answer_users_str += x
                    print(self.correct_answer_users_str + "PLESSASSDE")
                self.correct_answer_users_str += self.active_quiz.get_new_question() + "\n"
                print(self.correct_answer_users_str)
                return self.correct_answer_users_str
            else:
                print("THIS IS THE ELSEEEE")
                self.correct_answer_users_set.add(str(message.author.name))
        return
