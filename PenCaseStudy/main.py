from PenCaseStudy.pens.BalPen import BalPen
from PenCaseStudy.pens.Pen import Pen
from PenCaseStudy.write_strategies.Smooth_writestrategy import SmoothWriteStrategy


class Main:
    reynoldsTrimax= BalPen(SmoothWriteStrategy)
    print(reynoldsTrimax)