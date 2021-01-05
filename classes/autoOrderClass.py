from classes.bolComClass import bol

class autoOrder:
    def __init__(self, arguments):
        self.direct_pay = 0
        self.timeout = 120

        for current_argument, current_value in arguments:
            if current_argument in ("--email"):
                self.username = current_value
            elif current_argument in ("--password"):
                self.password = current_value
            elif current_argument in ("--productId"):
                self.product_id = current_value
                print("ProductId: " + str(current_value))
            elif current_argument in ("--timeout"):
                self.timeout = int(current_value)
            elif current_argument in ("--directorder"):
                self.direct_pay = 1


    def start(self):
        bolClass = bol(self.username, self.password)
        if bolClass.check_availabity_of_productId(self.product_id, self.timeout):
            print("Available !")
            bolClass.orderProductById(self.product_id, self.direct_pay)