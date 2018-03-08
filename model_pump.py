#!bin/python
# -*- coding: utf-8 -*-

from fun_piecewise import *
import math


class model_pump: # pump model

    def __init__(self, string_open_es_m, string_current_p):  # рассмотреть возможность подключения к базе по KKS

        self.string_open_es_m = string_open_es_m
        self.string_current_p = string_current_p

        self.open_es_m = 0  # Обратная связь ИМ, "включено" двигателя насоса (0-1)

        self.nominal_f = 444.0  # Номинальный расход, кг/с
        self.nominal_p = 10.53  # Номинальный перепад давления на напорной арматуре, МПа
        self.current_f = 0.0  # Расход текущий, кг/с
        self.current_p = 0.0  # Давление текущее, МПа
        self.density = 1000.0  # Текущая плотность перекачиваемой среды, кг/м3
        self.dp = []
        self.df = []

        # Характеристика насоса
        self.dh = [1074.05, 1036.77, 1035.04, 1028.10, 1020.65, 1001.99, 983.24, 965.84, 958.74, 928.47, 896.76, 890.31,
                   861.98, 825.49, 749.41]  # Напор, м
        self.dg = [0.0, 403.38, 575.36, 694.64, 820.54, 1010.52, 1158.00, 1308.16, 1518.56, 1691.59, 1825.59, 1840.90,
                   1940.31, 2069.06, 2294.10]  # Подача, м3/ч

        self.maximum_f = self.__get_dp_df()
        self.line_p = fun_piecewise(self.df, self.dp)

    def __get_dp_df(self):
        i = 0
        while i <= len(self.dh) - 1:
            self.dp.append(float(self.density * 9.80665 * self.dh[i] * 0.000001))  # Давление на напоре с учетом плотности, МПа
            i += 1

        i = 0
        while i <= len(self.dg) - 1:
            self.df.append(float((self.density * self.dg[i]) / 3600))  # Расход с учетом плотности, кг/с
            i += 1

        return self.df[len(self.df) - 1]

    def get_current_f(self, eas_p1, eas_p2, eas_rk, dt, k=1):
        if eas_p1 - eas_p2 >= 0.0:
            f = math.sqrt(eas_p1 - eas_p2) * (eas_rk / 100) * k
            if f >= self.df[len(self.df) - 1]:
                self.current_f = self.df[len(self.df) - 1]
            else:
                self.current_f = f
            # self.current_f = (math.sqrt(eas_p1 - eas_p2) * (eas_rk / 100)) * k # k=1250
            self.current_p = self.line_p.get_point(self.current_f)
            return self.current_f
        else:
            self.current_p = self.line_p.get_point(0.0)
            return 0.0
