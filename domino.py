from manimlib.imports import *


class Chessboard(VGroup):
    def __init__(self, m, n, s_width=1, s_length=1, **kwargs):
        VGroup.__init__(self, **kwargs)
        for x in range(0, m + 1):
            self.add(Line(
                s_width * np.array([x - (m/2), -(n/2), 0]),
                s_width * np.array([x - (m/2), (n/2), 0]))
                )
        for y in range(0, n + 1):
            self.add(Line(
                s_length * np.array([-(m/2), y - (n/2), 0]),
                s_length * np.array([(m/2), y - (n/2), 0]))
                )



class DominoScene(Scene):
    CONFIG = {
        "m": 5,
        "n": 4,
        "s_width": 1.5,
        "s_length": 1.5
    }
    def construct(self):
        self.table = Chessboard(self.m, self.n, s_width=self.s_width, s_length=self.s_length)
        self.add(self.table)