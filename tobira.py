import random
from n3 import tobira_questions
# tobira_questions = [('1', 'one'), ('2', 'two')]

rand_quest = 0

class Tobira:
    def __init__(self):
        self.question = tobira_questions[random.randint(0, len(tobira_questions) - 1)][0]
        self.answer = tobira_questions[random.randint(0, len(tobira_questions) - 1)][1]
        self.meaning = tobira_questions[random.randint(0, len(tobira_questions) - 1)][2]


    # Function that fetches new question
    def get_new_question(self):
        rand_quest = random.randint(0, (len(tobira_questions) - 1))
        self.question = tobira_questions[rand_quest][0]
        self.answer = tobira_questions[rand_quest][1]
        self.meaning = tobira_questions[rand_quest][2]
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
