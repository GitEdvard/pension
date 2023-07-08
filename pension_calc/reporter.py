import os
import shutil
import datetime
from contextlib import redirect_stdout
from pension_calc.calculator import Calculator
from pension_calc.definitions import PACKAGE_DIR
from pension_calc.presenter import Presenter
from pension_calc.config import CONFIG


class Reporter:
    @staticmethod
    def generate(identifier):
        file_name = identifier + "_" + Reporter.today() + ".txt"
        path= os.path.join(PACKAGE_DIR, "output", file_name)
        calculator = Calculator()
        presenter = Presenter()
        with open(path, "w", encoding="utf-8") as f:
            with redirect_stdout(f):
                print("Date: " + Reporter.today())
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
        backup_file_path = os.path.join(CONFIG.backup_catalog, file_name)
        shutil.copyfile(path, backup_file_path)

    @staticmethod
    def today():
        date = datetime.date.today()
        return date.strftime("%Y-%m-%d")
