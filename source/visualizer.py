# -*- coding:utf-8 -*-
# @Time: 2022/12/15 16:00
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: visualizer.py.py
from typing import TYPE_CHECKING
from Melodie import Visualizer
from source.data_info import id_health_state

if TYPE_CHECKING:
    from .model import CovidModel


class CovidVisualizer(Visualizer):
    model: 'CovidModel'

    def setup(self):
        self.add_visualize_component('network',
                                     'network',
                                     lambda: self.model.network,
                                     color_categories={
                                         0: {
                                             "label": "not_infected",
                                             "color": "#00fb34"
                                         },
                                         1: {
                                             "label": "infected",
                                             "color": "#fafb56"
                                         },
                                         2: {
                                             "label": "recovered",
                                             "color": "#3434b8"
                                         },
                                         3: {
                                             "label": "dead",
                                             "color": "#999999"
                                         }
                                     },
                                     roles_getter=lambda agent: agent.health_state)
