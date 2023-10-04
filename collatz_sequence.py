x = (int(input("Please enter intiger number from 1 to 100:" )))

while x < 1 or x > 100:
    print ("This value is not in the range!")
    x = (int(input("Please enter intiger number from 1 to 100:" )))

if x == 1:
    print("1")

while x !=1:

    if x % 2 == 0:
        x /= 2
        print(int(x))

    else:
        x = 3*x+1
        print(int(x))


