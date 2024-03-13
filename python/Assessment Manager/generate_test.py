import random
from datetime import datetime
import time
import os
import threading
import sys

class Question:
    def __init__(self, num1, num2, op, ans):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        self.ans = ans
    
    def __repr__(self) -> str:
        return str('num1: ' + str(self.num1) + ' num2: '+ str(self.num2))

class Test:
    
    def prepare_test(self):
        test_date = datetime.today().strftime('%b-%d-%Y')
        ends_in_zeroes = []
        for n in range(0, 100001, 10000):
            ends_in_zeroes.append(n)
        print(test_date)
        questions = []
        num1_cache = {}
        for _ in range(10):
            # num1 = random.randint(0, 99999)
            idx = random.randint(0, len(ends_in_zeroes))
            num1 = ends_in_zeroes[idx]
            num2 = random.randint(0, num1)
            num = Question(num1, num2, 'sub', None)
            questions.append(num)
        self.test_date = test_date
        self.questions = questions
        self.tick = 10
        print('Test prepared!')

    
    def start_test(self):
        for q in self.questions:
            print(f'\t{q.num1} \n - \n \t{q.num2}\n\t------------\n \n \t---------------')    
            q.ans = int(input('Enter your ans: '))
            os.system('cls')

    def start_timer(self):
        while self.tick > 0:
            time.sleep(1)
            self.tick -= 1
            if self.tick <= 5:
                print(f'Time remaining: {self.tick} seconds')
        print("Time's up!!!")
        self.evaluate_test()
        
    
    def evaluate_test(self):
        score = 0
        for q in self.questions:
            if q.op == 'sub':
                if q.ans == q.num1 - q.num2:
                    score += 1
        
        print('Score is ' + str(score) +'/10')
        if score <= 4:
            print('You need to practice more!!!')
        elif score <= 7:
            print('You can do better!!!')
        elif score <= 9:
            print('Good job!!!')
        else:
            print('Congrats on perfect 10!!!')


# class Countdown:
#     def __init__(self, tick):
#         countdown_thread = threading.Thread(target=self.run)
#         countdown_thread.daemon = True
#         self.tick = tick
#         countdown_thread.start()
#         print('Timer prepared')

#     def run(self):
#             print('Time to complete test: ' + str(self.tick) + ' seconds')
#             while self.tick > 0:
#                 time.sleep(1)
#                 self.tick -= 1
#                 if self.tick <= 5:
#                     print(f'Time remaining: {self.tick} seconds')
#             print("Time's up!!!")
#             sys.exit(0)

test = Test()
test.prepare_test()

test.start_test()
test.evaluate_test()