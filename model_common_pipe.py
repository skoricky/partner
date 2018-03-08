#!bin/python
# -*- coding: utf-8 -*-

class model_common_pipe: # pipe model

    def __init__(self, pipe_vol=150.0, completed_vol=140.0, out_p=7.0):
        self.pipe_vol = pipe_vol  # Общий объем коллектора/трубы, м3
        self.completed_vol = completed_vol  # Заполненный объем, м3
        self.density = 1000.0  # Текущая плотность перекачиваемой среды, кг/м3
        self.d_vol = 0.0  # Разовый объем, м3
        self.in_vol = [0.0]
        self.out_vol = [0.0]
        self.__out_vol_k = [0.0]  # Долевые коэффициенты исходящих расходов по характеристике клапанов/арматуры на выходе из коллектора/трубы
        self.current_out_p = self.__get_out_p(out_p)

    def __get_out_p(self, out_p):
        if self.get_sum_vol(self.out_vol) > 0.0:
            return out_p
        else:
            return 0.0

    def set_out_p(self, out_p):
        self.current_out_p = self.__get_out_p(out_p)
        return self.current_out_p  # давление на выходе из коллектора/трубы, МПа

    @staticmethod
    def get_sum_vol(vol):
        return sum((float(vol[i]) for i in range(0, int(len(vol)))))

    def get_common_vol(self, dt):
        k = 3600.0 / self.density
        d_vol = (self.get_sum_vol(self.in_vol) - self.get_sum_vol(self.out_vol)) * k
        vol = self.completed_vol + (self.d_vol + d_vol) / 2 * (dt / 1000)
        self.d_vol = d_vol

        if vol < self.pipe_vol * 1.01:
            self.completed_vol = vol
        else:
            self.completed_vol = self.pipe_vol * 1.01


