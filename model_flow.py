#!bin/python
# -*- coding: utf-8 -*-

import math


class model_flow:  # flow model

    def __init__(self, string_eas_p1='', string_eas_p2='', string_eas_rk=''):
        self.string_eas_rk = string_eas_rk
        self.string_eas_p1 = string_eas_p1
        self.string_eas_p2 = string_eas_p2
        self.eas_rk = 0.0
        self.eas_p1 = 0.0
        self.eas_p2 = 0.0
        self.density = 1000.0

        self.current_f = 0.0
        self.kv = 130.0  # максимальная пропускная способность запорного устройства, м3/ч

    def get_current_f(self, k=1):
        eas_rk = self.eas_rk
        eas_p1 = self.eas_p1
        eas_p2 = self.eas_p2
        kv = self.kv
        density = self.density / 1000
        maximum_f = kv * self.density / 3600

        if eas_p1 - eas_p2 >= 0.0:
            f = k * (eas_rk * kv / 100) * math.sqrt(density * (eas_p1 - eas_p2))
            if f >= maximum_f:
                self.current_f = maximum_f
            else:
                self.current_f = f
            return self.current_f
        else:
            return 0.0

