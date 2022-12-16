from Melodie import Simulator
from config import config
from source.data_loader import CovidDataLoader
from source.model import CovidModel
from source.scenario import CovidScenario
from source.visualizer import CovidVisualizer

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=CovidModel,
        scenario_cls=CovidScenario,
        data_loader_cls=CovidDataLoader,
        visualizer_cls=CovidVisualizer
    )
    simulator.run_visual()
