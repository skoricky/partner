#!bin/python
# -*- coding: utf-8 -*-

import math
from model_flow import *


class model_valve: # valve model

    def __init__(self, string_close_es_sk):

        self.string_close_es_sk = string_close_es_sk
        self.string_open_es_sk = string_close_es_sk[:-3] + string_close_es_sk[-3] + '32'
        self.string_aloe_sk = string_close_es_sk[:-3] + string_close_es_sk[-3] + '42'
        self.string_als_sk = string_close_es_sk[:-3] + string_close_es_sk[-3] + '43'

        self.pos_sk = 0.0  # Расчетная позиция арматуры на напоре (0.0-100.0), %
        self.travel_time_sk = 52.0  # Время хода напорной арматуры, с

    def get_pos_sk(self, pos_sk, aloe, als, weaf, wezu, dt, per=99.45, k=0.6981):
        trv_t = self.travel_time_sk * k
        d_pos = float(per / trv_t) * dt

        if weaf == 1:
            return 99.45

        if wezu == 1:
            return 0.0

        if aloe == 0 and als == 0:
            return pos_sk

        if aloe == 1:
            if float(pos_sk + d_pos) < 99.0 and weaf < 1:
                return float(pos_sk + d_pos)
            else:
                return per
        else:
            if float(pos_sk - d_pos) > 0.9 and wezu < 1:
                return float(pos_sk - d_pos)
            else:
                return 0.0
