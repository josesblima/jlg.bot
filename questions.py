import random
from n5 import n5
from n4 import n4
from n3 import n3
from n2 import n2
from n1 import n1
# tobira_questions = [('1', 'one'), ('2', 'two')]

rand_quest = 0

class Questions:
    def __init__(self):
        self.cur_quiz = n3
        self.question = self.cur_quiz[random.randint(0, len(self.cur_quiz) - 1)][0]
        self.answer = self.cur_quiz[random.randint(0, len(self.cur_quiz) - 1)][1]
        self.meaning = self.cur_quiz[random.randint(0, len(self.cur_quiz) - 1)][2]


    # Function that fetches new question
    def get_new_question(self):
        rand_quest = random.randint(0, (len(self.cur_quiz) - 1))
        self.question = self.cur_quiz[rand_quest][0]
        self.answer = self.cur_quiz[rand_quest][1]
        self.meaning = self.cur_quiz[rand_quest][2]
        return (self.question)

    def get_question(self):
        return self.question
    def get_answer(self):
        return self.answer
    def get_meaning(self):
        return self.meaning
    # Checks if answer is right
    def check_answer(self, message):
        p_message = message.content.lower()
        if (p_message == self.answer):
            return True
        return False

    def n5(self):
        self.cur_quiz = n5
    def n4(self):
        self.cur_quiz = n4
    def n3(self):
        self.cur_quiz = n3
    def n2(self):
        self.cur_quiz = n2
    def n1(self):
        self.cur_quiz = n1







# 東京
# 京都
# 地図
# 国土
# 南北
# 南
# 北
# 機構
# 気温
# 摂氏
# 桜
# 壁
# 白鷺
# 広げる
# 撮影
# 火山
# 観光
# 温泉
# 景色
# 露天風呂
# 歴史
# 小説
# 旅館
# 土産話
