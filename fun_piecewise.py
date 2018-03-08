#!bin/python
# -*- coding: utf-8 -*-

class fun_piecewise: # piecewise function

    def __init__(self, in_x, in_y):

        self._in_x = in_x
        self._in_y = in_y

    def output_y(self, x1, x2, y1, y2, x):
        return (((x - x1) * (y2 - y1)) / (x2 - x1)) + y1

    def get_point(self, x):
        if x < self._in_x[0]:
            return self._in_y[0]
        if x > self._in_x[len(self._in_x) - 1]:
            return self._in_y[len(self._in_x) - 1]
        i = 0
        while i < len(self._in_x) - 1:
            if x <= self._in_x[i + 1]:
                if x >= self._in_x[i]:
                    return self.output_y(self._in_x[i], self._in_x[i + 1], self._in_y[i], self._in_y[i + 1], x)
            else:
                i += 1
