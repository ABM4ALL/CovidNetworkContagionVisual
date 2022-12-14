from Melodie import Scenario
from source import data_info


class CovidScenario(Scenario):

    def setup(self):
        self.period_num: int = 0
        self.agent_num: int = 0
        self.network_type: str = ""
        self.network_param_k: int = 0
        self.network_param_p: float = 0.0
        self.network_param_m: int = 0
        self.initial_infected_percentage: float = 0.0
        self.young_percentage: float = 0.0
        self.infection_prob: float = 0.0
        self.setup_transition_probs()

    def get_network_params(self):
        if self.network_type == "barabasi_albert_graph":
            network_params = {"m": self.network_param_m}
        elif self.network_type == "watts_strogatz_graph":
            network_params = {"k": self.network_param_k, "p": self.network_param_p}
        else:
            raise NotImplementedError
        return network_params

    def setup_transition_probs(self):
        df = self.get_dataframe(data_info.transition_prob)
        self.transition_probs = {
            0: {
                "s1_s1": df.at[0, "prob_s1_s1"],
                "s1_s2": df.at[0, "prob_s1_s2"],
                "s1_s3": df.at[0, "prob_s1_s3"],
            },
            1: {
                "s1_s1": df.at[1, "prob_s1_s1"],
                "s1_s2": df.at[1, "prob_s1_s2"],
                "s1_s3": df.at[1, "prob_s1_s3"],
            }
        }

    def get_transition_probs(self, id_age_group: int):
        return self.transition_probs[id_age_group]
