from enum import Enum

class QuestionType(Enum):
	MULTIPLE_CHOICE = 0,
	TEXT = 1

class Question:
    def __init__(self, question_type, prerequesits, body, answers, priority):
        self.question_type = question_type
        self.prerequesits = prerequesits
        self.body = body
        self.answers = answers
        self.priority = priority

    def questions_queue_factory(self):
        questions_queue = [
            Question(QuestionType.MULTIPLE_CHOICE, [("Linear Model", True)], "Would you like to predict the future course of the variable?",
                [("Yes", ("PredictFuture", True)), ("No", ("PredictFuture", False))] , 1)
            #....
        ]
        return questions_queue
