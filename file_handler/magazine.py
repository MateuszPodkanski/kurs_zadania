from file_handler import FileHandler

file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")

print("magazine: ")
for item in file_handler.magazine:
    name = item.get("name")
    amount = item.get("amount")
    print(f"name:{name}, amount: {amount}")

