from questions import Questions
from database import Database
import asyncio

class Quiz:
    def __init__(self):
        self.active_quiz = None
        self.timer_sleep = False
        self.correct_answer_users_set = set()
        self.correct_answer_users_str = ""
        self.total_scores = {}
        self.total_scores_str = "Quiz ended, congratulations!"
        self.end = False
        self.quiz_len = 2
        self.db = Database()

    def end_quiz(self):
        self.active_quiz = None
        self.timer_sleep = False
        self.correct_answer_users_set = set()
        self.correct_answer_users_str = ""
        self.total_scores = {}
        self.total_scores_str = "Quiz ended, congratulations!"
        self.end = False

    def quiz_starter(self, message):
        p_message = message.content.lower()
        if (p_message == 'n5'):
            self.active_quiz = Questions()
            print("quiz_starter\n")
            self.active_quiz.n5()
            return self.active_quiz.get_new_question()
        if (p_message == 'n4'):
            self.active_quiz = Questions()
            print("quiz_starter\n")
            self.active_quiz.n4()
            return self.active_quiz.get_new_question()
        if (p_message == 'n3'):
            self.active_quiz = Questions()
            print("quiz_starter\n")
            self.active_quiz.n3()
            return self.active_quiz.get_new_question()
        if (p_message == 'n2'):
            self.active_quiz = Questions()
            print("quiz_starter\n")
            self.active_quiz.n2()
            return self.active_quiz.get_new_question()
        if (p_message == 'n1'):
            self.active_quiz = Questions()
            print("quiz_starter\n")
            self.active_quiz.n1()
            return self.active_quiz.get_new_question()

    async def quiz_handler(self, message):
        p_message = message.content.lower()
        if self.active_quiz.check_answer(message) == True:
            if self.timer_sleep == False:
                return await self.sleep_timer(message)
            else:
                print("THIS IS THE ELSEEEE")
                # Update correct answers set
                self.correct_answer_users_set.add(str(message.author.name))
                # Update total scores dic
                if str(message.author.name) in self.total_scores:
                    self.total_scores[str(message.author.name)] += 1
                    if self.total_scores[str(message.author.name)] == self.quiz_len:
                        self.end = True
                else:
                    self.total_scores[str(message.author.name)] = 1
        elif p_message == 'skip':
            question = self.active_quiz.get_question()        
            answer = self.active_quiz.get_answer()        
            meaning = self.active_quiz.get_meaning()
            return question + ": " + answer + " -- " + meaning + "\n" + self.active_quiz.get_new_question()
 
        return

    async def sleep_timer(self, message):
        self.correct_answer_users_str = ""
        # Update correct answer set
        self.correct_answer_users_set.add(str(message.author.name))
        # Update total scores dic
        if str(message.author.name) in self.total_scores:
            self.total_scores[str(message.author.name)] += 1
            if self.total_scores[str(message.author.name)] == self.quiz_len:
                self.end = True
        else:
            self.total_scores[str(message.author.name)] = 1
        self.timer_sleep = True
        await asyncio.sleep(2)
        self.timer_sleep = False
        for x in self.correct_answer_users_set:
            self.correct_answer_users_str += "\n" + x
        self.correct_answer_users_set = set()
        # Quiz end
        if self.end == True:
            self.active_quiz == None
            self.end = False
            for key, val in self.total_scores.items():
                self.total_scores_str += "\n" + key + ": " + str(val) + " points"
            return self.db.xpgold_update(message.author, 1, 1) + "\n" + self.total_scores_str
        print("right BEFORE return")
        question = self.active_quiz.get_question()        
        answer = self.active_quiz.get_answer()        
        meaning = self.active_quiz.get_meaning()
        self.correct_answer_users_str += "\n" + self.active_quiz.get_new_question()
        return question + ": " + answer + " -- " + meaning + "\n" + self.db.xpgold_update(message.author, 1, 1) + self.correct_answer_users_str
