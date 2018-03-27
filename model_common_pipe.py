#!bin/python
# -*- coding: utf-8 -*-

from model_density import *

class model_common_pipe: # pipe model

    def __init__(self, pipe_vol=150.0, completed_vol=140.0, out_p=7.0):
        self.pipe_vol = pipe_vol  # Общий объем коллектора/трубы, м3
        self.completed_vol = completed_vol  # Заполненный объем, м3
        self.density = 1000.0  # Текущая плотность перекачиваемой среды, кг/м3
        self.d_vol = 0.0  # Мгновенный объем, м3
        self.in_vol = [0.0]
        self.out_vol = [0.0]

        # Долевые коэффициенты исходящих расходов по характеристике клапанов/арматуры
        # на выходе из коллектора/трубы
        self.__out_vol_k = [0.0]

        # Текущее давление в коллекторе/трубе
        self.current_out_p = self.__get_out_p(out_p)

    @staticmethod
    def get_current_dencity(t=20):
        _density = density()
        return _density.get_density(t)  # Плотность воды от текущей температуры, кг/м3

    @staticmethod
    def get_sum_vol(vol):
        return sum((float(vol[i]) for i in range(0, int(len(vol)))))

    def get_single_flow(self, vol):
        sum_vol = self.get_sum_vol(vol)
        single_vol = []
        for i in range(0, int(len(vol))):
            if vol[i] < sum_vol / (len(vol) - 1):
                single_vol.append(vol[i])
            else:
                single_vol.append(sum_vol / (len(vol) - 1))
        return single_vol

    def __get_out_p(self, out_p):
        if self.get_sum_vol(self.out_vol) > 0.0:
            return out_p
        else:
            return 0.0

    def set_out_p(self, out_p):
        self.current_out_p = self.__get_out_p(out_p)
        return self.current_out_p  # давление в коллекторе/трубе, МПа

    def get_common_vol(self, in_vol, out_vol, dt, t=20):  # t = 20 градусов по умолчанию, плотность 1000 кг/м3
        self.density = self.get_current_dencity(t)
        k = 3600.0 / self.density
        d_vol = (self.get_sum_vol(in_vol) - self.get_sum_vol(out_vol))
        vol = self.completed_vol + (self.d_vol + d_vol) / 2 * (dt / 1000) * k
        self.d_vol = d_vol

        if vol < self.pipe_vol * 1.01:
            self.completed_vol = vol
        else:
            self.completed_vol = self.pipe_vol * 1.01


