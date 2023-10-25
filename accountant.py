import sys

history = ["saldo 10000 zyski","saldo -2000 podatek","zakup car 20000 5"]
saldo = 10000
combined_arguments = " ".join(sys.argv[1:])
arguments = sys.argv[1:]


magazine = [{"id": 1,
             "name": "car",
             "amount": "5"},

            {"id": 2,
             "name": "boat",
             "amount": "5"},
             
            {"id": 3,
             "name": "motor",
             "amount": "5"}]

operation = sys.argv[1]

if operation == "saldo":
    saldo += int(sys.argv[2])
    history.append(combined_arguments)

elif operation == "zakup":
    name_zakup = sys.argv[2]
    price_zakup = int(sys.argv[3])
    amount_zakup = int(sys.argv[4])

    full_price = price_zakup * amount_zakup
    saldo -= full_price
    
    if saldo < 0 or price_zakup < 0 or amount_zakup < 0:
        print ("Price, amount of products bought and saldo can't be below 0 ")

    for item in magazine:
        if name_zakup == item["name"]:
            new_amount = int(item["amount"]) + amount_zakup
            item["amount"] = str(new_amount)
            history.append(combined_arguments)
            break
        else:
            print ("Item like that is not included in magazine!")

elif operation == "sprzedaż":
    name_sprzedaż = sys.argv[2]
    price_sprzedaż = int(sys.argv[3])
    amount_sprzedaż = int(sys.argv[4])
    full_price = price_sprzedaż * amount_sprzedaż

    if price_sprzedaż < 0 or amount_sprzedaż < 0:
        print("Price and amount can't be below 0!")
    else:    
        for item in magazine:
            if name_sprzedaż == item["name"]:
                if int(item["amount"]) >= amount_sprzedaż:
                    new_amount = int(item["amount"]) - amount_sprzedaż 
                    item["amount"] = str(new_amount)
                    saldo += full_price
                    history.append(combined_arguments)
                    break
                else:
                    print("There is not enough items like that in magazine!")
                    break
        else:
            print ("Item like that is not included in magazine!")


elif operation == "konto":
    print(saldo)

elif operation == "magazyn":
    
    for items in magazine:
        if items["name"] in arguments:
            print(f"ID: {items['id']}, Name: {items['name']}, Amount: {items['amount']}")

elif operation == "przegląd":
    start_index = int(sys.argv[2])
    end_index = int(sys.argv[3])
    if 0 <= start_index < len(history) and 0 <= end_index < len(history):
        for i in range(start_index,end_index+1):
            print(f'{history[i]}')
    else:
        print("Invalid history range!")

else:
    print("Error, allowed operations are: zakup, sprzedaż, saldo, konto, przegląd and magazyn")
