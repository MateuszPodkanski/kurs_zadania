from file_handler import FileHandler

file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")

print("history :")

for element in file_handler.history:
    print(element)

