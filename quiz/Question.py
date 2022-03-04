class Decision:
    def __init__(self):
        pass
    
    def check_answer(self, default, chosen):
        if default == chosen:
            print("Wow you got it right")
        else:
            print("Try your luck next time")

            
class Question (Decision):
    def __init__(self):
        self.option = "prince"
        self.status = 0
        super().__init__()
    
    def first_question(self):
        self.option = int(input('Nelson Mandela died in 2012 (1-True or 0-False) : '))
        self.status = 0

        super().check_answer(self.option, self.status)


    def second_question(self):
        self.option = int(input('Corona virus was discovered in 2019 (1-True or 0-False) : '))
        self.status = 1

        super().check_answer(self.option, self.status)


question = Question()
question.first_question()
question.second_question()