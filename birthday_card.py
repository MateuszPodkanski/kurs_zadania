from datetime import date

print ("Hello, let's write greetings card together!")
print (" ")


name_a = input("Please enter reciever's name: ")
year = int(input("Please provide reciever's year of birth: "))
month = int(input("Next, reciever's month of birth: "))
day = int(input("Lastly, reciever's day of birth: "))
message = input("Enter message you would like to send: ")
name_b = input("Please enter sender's name: ")

today = date.today()
birthday = date(year, month, day)

age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

print(f"""{name_a}, wszystkiego najlepszego z okazji {age}. urodzin!

{message}

{name_b}""")