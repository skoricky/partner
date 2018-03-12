#!bin/python
# -*- coding: utf-8 -*-

import math


class model_df: # flow model

    def __init__(self, string_eas_p1='', string_eas_p2='', string_eas_rk=''):
        self.string_eas_rk = string_eas_rk
        self.string_eas_p1 = string_eas_p1
        self.string_eas_p2 = string_eas_p2
        self.eas_rk = 0.0
        self.eas_p1 = 0.0
        self.eas_p2 = 0.0
        self.density = 1000.0

        self.current_f = 0.0
        self.kv = 130.0

    def get_current_f(self, k=1):
        eas_rk = self.eas_rk
        eas_p1 = self.eas_p1
        eas_p2 = self.eas_p2
        kv = self.kv
        density = self.density / 1000
        maximum_f = kv * self.density / 3600

        if eas_p1 - eas_p2 >= 0.0:
            f = (eas_rk / 100 * kv) * math.sqrt(density * (eas_p1 - eas_p2)) * k
            if f >= kv * maximum_f:
                self.current_f = maximum_f
            else:
                self.current_f = f
            return self.current_f
        else:
            return 0.0

