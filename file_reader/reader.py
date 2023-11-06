import sys
import csv
import os


class File_Reader:

    def __init__(self,beginning_file,end_location,changes):
        self.beginning_file = beginning_file
        self.end_location = end_location
        self.changes = changes
        self.beginning = self.reading_and_changing_file()
        self.end = self.writing_end_file()


    def reading_and_changing_file(self):
        lines = []
        with open(self.beginning_file, newline="") as f:
            reader = csv.reader(f)
            for line in reader:
                 lines.append(line[0].split(';')) 

        
        for change in self.changes:
            row, column, value = map(str, change.split(","))
            row, column = int(row)-1, int(column)-1
            
            if row < len(lines) and column < len(lines[0]): 
                lines[row][column] = value
            else:
                print(f"Change ignored: Row or Column index out of range for change {change}")

            for line in lines:
                print(';'.join(line))
            return lines

    def writing_end_file(self):
        with open(self.end_location, 'w') as f:
            for line in self.beginning:
                f.write(';'.join(line) + '\n')

def program_start():
    while True:
        if os.path.exists(sys.argv[1]) :
            reader = File_Reader(beginning_file = sys.argv[1],end_location = sys.argv[2],changes = sys.argv[3:])
            break
        else:
            sys.argv[1] = input("This path does not exist,please enter correct path: \n")

program_start()