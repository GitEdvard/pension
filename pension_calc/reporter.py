import os
from pension_calc.definitions import PACKAGE_DIR


class Reporter:
    @staticmethod
    def generate(file_name):
        path= os.path.join(PACKAGE_DIR, "output", file_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write("hej\n")
