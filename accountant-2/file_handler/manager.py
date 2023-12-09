from file_handler import FileHandler
import sys

class Manager:
    def __init__(self):
        self.actions={}

    def assign(self,name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate
    
    def execute(self,name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)

manager = Manager()

@manager.assign("change saldo")
def change_saldo(manager):
    saldo_file = sys.argv[0]
    file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")
    file_handler.change_saldo(sys.argv[1])
    file_handler.save_to_saldo()
    combined_arguments = FileHandler.combine_arguments()
    file_handler.add_history(combined_arguments)
    file_handler.save_to_history()

@manager.assign("sell operation")
def sell_operation(manager):
    file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")
    file_handler.change_magazine()
    file_handler.save_to_saldo()
    file_handler.save_to_magazine()
    combined_arguments = FileHandler.combine_arguments()
    file_handler.add_history(combined_arguments)
    file_handler.save_to_history()

@manager.assign("buy operation")
def buy_operation(manager):
    file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")
    file_handler.change_magazine()
    file_handler.save_to_saldo()
    file_handler.save_to_magazine()
    combined_arguments = FileHandler.combine_arguments()
    file_handler.add_history(combined_arguments)
    file_handler.save_to_history()

@manager.assign("show history")
def show_history(manager):
    file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")

    print("history :")

    for element in file_handler.history:
        print(element)

@manager.assign("show account")
def show_account(manager):
    
    file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")

    print (f"saldo: {file_handler.saldo}")

@manager.assign("show magazine")
def show_magazine(manager):
    
    file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")

    print("magazine: ")
    for item in file_handler.magazine:
        name = item.get("name")
        amount = item.get("amount")
        print(f"name:{name}, amount: {amount}")



