from Python_Selenium.Config import Config
from Python_Selenium.Utility import Utility
from Python_Selenium.Steps import Steps

class Testcases:
    steps = Steps.element
    def login_testcase(self):

        act_title=self.steps.title
        self.exp_title = "Amazon Sign In"
        if(act_title==self.exp_title):
                print("Login Test Pass")
        else:
                print("Login Test Fail")

config = Config()
utility = Utility()
steps = Steps()
# steps.Login_steps()
steps.add_to_cart()
testcases = Testcases()
testcases.login_testcase()