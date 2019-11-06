class Question:
    def __init__(self):
        self.question_text = ""
        self.pub_date = ""

    def __str__(self):
        return self.question_text

    __repr__ = __str__
