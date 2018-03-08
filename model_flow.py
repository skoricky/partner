#!bin/python
# -*- coding: utf-8 -*-

import math


class model_df: # flow model

    def __init__(self, string_eas_p1='', string_eas_p2='', string_eas_rk=''):
        self.string_eas_rk = string_eas_rk
        self.string_eas_p1 = string_eas_p1
        self.string_eas_p2 = string_eas_p2
        self.density = 1000.0

        self.current_f = 0.0
        self.maximum_f = 250.0

    def get_current_f(self, eas_p1, eas_p2, eas_rk, k=1):
        if eas_p1 - eas_p2 >= 0.0:
            f = (0.25 * 3.14159 * math.pow(eas_rk, 2) / 100) * math.sqrt(2 * self.density * (eas_p1 - eas_p2)) * k
            if f >= self.maximum_f:
                self.current_f = self.maximum_f
            else:
                self.current_f = f
            return self.current_f
        else:
            return 0.0

