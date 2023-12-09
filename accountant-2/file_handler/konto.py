from file_handler import FileHandler

file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")

print (f"saldo: {file_handler.saldo}")

