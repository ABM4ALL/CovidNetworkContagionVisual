import random
from typing import TYPE_CHECKING

from Melodie import NetworkAgent

if TYPE_CHECKING:
    from source.scenario import CovidScenario
    from Melodie import AgentList
    from source.grid import CovidSpot
    from source.grid import CovidGrid


class CovidAgent(NetworkAgent):
    scenario: "CovidScenario"

    def set_category(self):
        self.category = 0

    def setup(self):
        self.health_state: int = 0
        self.age_group: int = 0

    def infection(self, agents: "AgentList[CovidNetworkAgent]"):
        neighbors = self.network.get_neighbors(self)
        for neighbor_category, neighbor_id in neighbors:
            neighbor_agent: "CovidAgent" = agents.get_agent(neighbor_id)
            if neighbor_agent.health_state == 1:
                if random.uniform(0, 1) < self.scenario.infection_prob:
                    self.health_state = 1
                    break

    def health_state_transition(self):
        if self.health_state == 1:
            transition_probs: dict = self.scenario.get_transition_probs(self.age_group)
            rand = random.uniform(0, 1)
            if rand <= transition_probs["s1_s1"]:
                pass
            elif transition_probs["s1_s1"] < rand <= transition_probs["s1_s1"] + transition_probs["s1_s2"]:
                self.health_state = 2
            else:
                self.health_state = 3
