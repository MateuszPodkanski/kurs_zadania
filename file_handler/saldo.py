from file_handler import FileHandler
import sys


saldo_file = sys.argv[0]
file_handler = FileHandler(saldo_file="saldo.json", history_file= "history.json", magazine_file="magazine.json")
file_handler.change_saldo(sys.argv[1])
file_handler.save_to_saldo()
combined_arguments = FileHandler.combine_arguments()
file_handler.add_history(combined_arguments)
file_handler.save_to_history()


