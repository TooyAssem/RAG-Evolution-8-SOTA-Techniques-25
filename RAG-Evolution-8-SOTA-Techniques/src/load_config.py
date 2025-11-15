import yaml
from pyprojroot import here
from box import Box


class APPConfig:
    def __init__(self):
        self._config_path = here("configs/config.yml")
        self._config = None

    def load(self) -> Box:
        """Load the application configuration from the YAML file."""
        if self._config is None:
            with open(self._config_path, "r") as f:
                self._config = yaml.safe_load(f)
        return Box(self._config)
