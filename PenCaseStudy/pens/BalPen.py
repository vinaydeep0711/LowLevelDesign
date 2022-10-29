from PenCaseStudy.pens.Pen import Pen
from PenCaseStudy.Refil import Refil


class BalPen(Pen):
    def __init__(self, writeStrategy):
        self.refil = Refil
        self.writestrategy = writeStrategy

    def get_refil(self):
        return self.refil

    def write(self):
        return self.writestrategy

