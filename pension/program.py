import os
import yaml

class Config:
    def __init__(self):
        pass

    def open_config(self):
        here = os.path.dirname(__file__)
        path = os.path.join(here, 'resources/data.yml')
        with open(path, 'r') as file:
            config = yaml.load(file)
        name = config["name"]
        print(f"name: {name}")
        return config
