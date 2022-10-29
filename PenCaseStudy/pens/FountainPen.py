from PenCaseStudy.pens.Pen import Pen
from PenCaseStudy.Ink import Ink
from PenCaseStudy.Nib import Nib


class FountainPen(Pen):

    def __init__(self):
        self.nib = Nib
        self.Ink = Ink

    def write(self):
        pass
