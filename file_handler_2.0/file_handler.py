import pickle
from abc import abstractmethod
import json
import csv


class FileHandler:
    def __init__(self,arguments):
        self.input_file = arguments[1]
        self.output_file = arguments[2]
        self.changes = arguments[3:]
        self.data = None

    @abstractmethod
    def read_data_from_file(self):
        raise NotImplementedError("You didn't implement an option to open this type of file")

    @abstractmethod
    def write_data_to_file(self):
        raise NotImplementedError("You didn't implement an option to open this type of file")

    def change_data_as_per_changes(self):
        for change in self.changes:
            x_value, y_value, new_field = change.split(",")
            x_index, y_index = int(x_value), int(y_value)
            self.data[x_index][y_index] = new_field


class TxTFileHandler(FileHandler):


    def read_data_from_file(self):
        temporary_data = []
        with open(self.input_file) as file:
            for line in file:
                temporary_data.append([field.strip() for field in line.split(",")])
        self.data = temporary_data

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            for line in self.data:
                file.write(",".join(map(str,line)))
                file.write("\n")


    
class PickleFileHandler(FileHandler):

    def read_data_from_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data = pickle.load(file)
    
    def write_data_to_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.data,file)

class JsonFileHandler(FileHandler):

    def read_data_from_file(self):
        with open(self.input_file, mode="r") as file:
            self.data = json.loads(file.read())

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            json.dump(self.data,file)

class CSVFileHandler(FileHandler):

    def read_data_from_file(self):
        temporary_data = []
        with open(self.input_file, mode="r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                temporary_data.append(row)
        self.data = temporary_data

    
    def write_data_to_file(self):
        with open(self.output_file, mode="w", newline = '') as file:
            csv_writer = csv.writer(file,delimiter = ',')
            for row in self.data:
                csv_writer.writerow(row)


 


    