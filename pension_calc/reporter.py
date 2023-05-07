import os
import pension_calc


class Reporter:
    @staticmethod
    def generate(file_name):
        base = os.path.dirname(pension_calc.__file__)
        path= os.path.join(base, "../output", file_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write("hej\n")
