# -*- coding:utf-8 -*-
# @Time: 2022/12/15 16:00
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: visualizer.py.py
from typing import TYPE_CHECKING
from Melodie import FloatParam, Visualizer
from source.data_info import id_health_state

if TYPE_CHECKING:
    from .model import CovidModel


class CovidVisualizer(Visualizer):
    model: 'CovidModel'

    def setup(self):
        self.params_manager.add_param(
            FloatParam('infection_prob', (0, 0.2), 9, label="Infection Probability (%)"),
        )

        self.plot_charts.add_line_chart("line").set_data_source({
            "not_infected": lambda: self.model.environment.s0,
            "infected": lambda: self.model.environment.s1,
            "recovered": lambda: self.model.environment.s2,
            "dead": lambda: self.model.environment.s3
        })

        self.plot_charts.add_barchart('bar').set_data_source(
            {
                "not_infected": lambda: self.model.environment.s0,
                "infected": lambda: self.model.environment.s1,
                "recovered": lambda: self.model.environment.s2,
                "dead": lambda: self.model.environment.s3
            })

        self.add_network('network',
                         lambda: self.model.network,
                         var_getter=lambda agent: agent.health_state,
                         var_style={
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
                         }, )
