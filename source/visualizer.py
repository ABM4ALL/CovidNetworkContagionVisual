from typing import TYPE_CHECKING
from Melodie import FloatParam, Visualizer

if TYPE_CHECKING:
    from source.model import CovidModel


class CovidVisualizer(Visualizer):
    model: "CovidModel"

    def setup(self):
        self.params_manager.add_param(FloatParam(
            name='infection_prob',
            value_range=(0, 1),
            label="Infection Probability (%)"
        ))

        self.plot_charts.add_line_chart("infection_count_line").set_data_source({
            "not_infected": lambda: self.model.environment.s0,
            "infected": lambda: self.model.environment.s1,
            "recovered": lambda: self.model.environment.s2,
            "dead": lambda: self.model.environment.s3
        })

        self.plot_charts.add_barchart('infection_count_bar').set_data_source({
            "not_infected": lambda: self.model.environment.s0,
            "infected": lambda: self.model.environment.s1,
            "recovered": lambda: self.model.environment.s2,
            "dead": lambda: self.model.environment.s3
        })

        self.add_network(name='covid_contagion_network',
                         network_getter=lambda: self.model.network,
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
                         })
