import sys
import json
import os

class FileHandler:

    def __init__(self,saldo_file,history_file,magazine_file):
        self.magazine_file = magazine_file
        self.saldo_file = saldo_file
        self.history_file = history_file
        self.magazine = self.read_from_magazine_file()
        self.history = self.read_from_history_file()
        self.saldo = self.read_from_saldo_file()
    

    def read_from_magazine_file(self):
        with open (self.magazine_file) as file:
            temporary_magazine = json.loads(file.read())
            temporary_magazine = temporary_magazine['magazine ']
            return temporary_magazine
        
    def read_from_history_file(self):
        with open (self.history_file) as file:
            temporary_history = json.loads(file.read())
            return temporary_history.get("history ")
    
    def read_from_saldo_file(self):
        with open (self.saldo_file) as file:
            temporary_saldo = json.loads(file.read())
            return temporary_saldo.get("saldo ")
    
    def change_saldo(self, new_saldo):
        self.saldo += int(new_saldo)
        if int(self.saldo) < 0:
            self.saldo -= int(new_saldo)
            print("Not enough money on the account!")
            sys.exit

    @staticmethod
    def combine_arguments():
        file_name=os.path.splitext(sys.argv[0])[0]
        combined_arguments = " ".join(sys.argv[1:])
        combined_arguments = f"{file_name} {combined_arguments}"
        return combined_arguments

    def change_magazine(self):
        sys.argv[0]=os.path.splitext(sys.argv[0])[0]

        operation_name = sys.argv[0]
        item_name = sys.argv[1]
        item_price = int(sys.argv[2])
        item_amount = int(sys.argv[3])
        full_price = item_price * item_amount
       
        if item_price < 0 or item_amount < 0:
            print("Item price and amount can't be below 0!")
            sys.exit

        if operation_name == "zakup":
            full_price = -(full_price)
            self.change_saldo(full_price)
            for item in self.magazine:
                if item.get("name") == item_name:
                    magazine_amount = int(item.get("amount"))
                    item["amount"] = str(magazine_amount + item_amount)
                else:
                    self.change_saldo(full_price)


        if operation_name == "sprzedaż":
            for item in self.magazine:
                if item.get("name") == item_name:
                    magazine_amount = int(item.get("amount"))
                    item["amount"] = str(magazine_amount - item_amount)
                    if int(item.get("amount")) < 0:
                        item["amount"] = str(magazine_amount)
                        print("Not enough products in the magazine!")
                        sys.exit
                    else:
                        self.change_saldo(full_price)
            

    def add_history(self, new_history):
        self.history.append(new_history)

    def save_to_history(self):
        with open (self.history_file, mode="w+") as file:
            file.write(json.dumps({"history ": self.history}))

    def save_to_magazine(self):
        with open (self.magazine_file, mode="w+") as file:
            file.write(json.dumps({"magazine ": self.magazine}))

    def save_to_saldo(self):
        with open (self.saldo_file, mode="w+") as file:
            file.write(json.dumps({"saldo ": self.saldo}))

    
            