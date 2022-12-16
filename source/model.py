from typing import TYPE_CHECKING

from Melodie import Model

from source import data_info
from source.agent import CovidAgent
from source.data_collector import CovidDataCollector
from source.environment import CovidEnvironment
from source.scenario import CovidScenario

if TYPE_CHECKING:
    from Melodie import AgentList


class CovidModel(Model):
    scenario: "CovidScenario"

    def create(self):
        self.agents: "AgentList[CovidAgent]" = self.create_agent_list(CovidAgent)
        self.environment: CovidEnvironment = self.create_environment(CovidEnvironment)
        self.data_collector = self.create_data_collector(CovidDataCollector)
        self.network = self.create_network()

    def setup(self):
        self.agents.setup_agents(
            agents_num=self.scenario.agent_num,
            params_df=self.scenario.get_dataframe(data_info.agent_params),
        )
        self.network.setup_agent_connections(
            agent_lists=[self.agents],
            network_type=self.scenario.network_type,
            network_params=self.scenario.get_network_params(),
        )

    def run(self):
        for period in self.iterator(self.scenario.period_num):
            self.environment.agents_infection(self.agents)
            self.environment.agents_health_state_transition(self.agents)
            self.environment.calc_population_infection_state(self.agents)
            self.data_collector.collect(period)
        self.data_collector.save()
