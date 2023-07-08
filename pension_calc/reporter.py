import os
from contextlib import redirect_stdout
from pension_calc.calculator import Calculator
from pension_calc.definitions import PACKAGE_DIR
from pension_calc.presenter import Presenter
from pension_calc.config import CONFIG


class Reporter:
    @staticmethod
    def generate(file_name):
        path= os.path.join(PACKAGE_DIR, "output", file_name)
        calculator = Calculator()
        presenter = Presenter()
        with open(path, "w", encoding="utf-8") as f:
            with redirect_stdout(f):
                print("------------------------------------------------")
                print("Balance")
                print("------------------------------------------------")
                p = calculator.balance()
                presenter.balance(p)
                print("")
                print("------------------------------------------------")
                print("Accomodation now")
                print("------------------------------------------------")
                p = calculator.accomodation_cost_now()
                presenter.accomodation_now(p)
                print("")
                print("------------------------------------------------")
                print("Accomodation at pension")
                print("------------------------------------------------")
                p = calculator.accomodation_cost_pension()
                presenter.accomodation_pension(p)
                print("")
                print("------------------------------------------------")
                print("Economic growth until pension")
                print("------------------------------------------------")
                p = calculator.return_on_savings()
                presenter.growth(p)
                print("")
                print("------------------------------------------------")
                print("Payment at pension")
                print("------------------------------------------------")
                p = calculator.pension_payment()
                presenter.payment(p)
                print("")
                print("------------------------------------------------")
                print("Config")
                print("------------------------------------------------")
                print(CONFIG)
                print("")
