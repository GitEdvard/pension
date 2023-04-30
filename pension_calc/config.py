import os
import yaml

class Config:
    def __init__(self):
        pass

    def open(self):
        here = os.path.dirname(__file__)
        path = os.path.join(here, '/home/edvard/sources/real/pension/resources/data.yml')
        with open(path, 'r') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        return config
