elements_number = int(input("Please enter number of elements to load: ")) 
packages_number = 0
current_package_weight = 0
packages_kilograms = 0
wasted_kilograms = 0
biggest_waste = 0

for number in range(0,elements_number):

    element_weight = (float(input("Please add next element weight in kg (0 if there is nothing left):")))

  #zrobiłem tutaj dodatkowego loopa żeby użytkownik od razu mógł naprawić swój błąd nie tracąc poprzednich 
  #rezultatów, można ją usunąc i zrobić sam warunek wtedy program skończy się na princie błędu  
    while element_weight >10 or element_weight <1 and element_weight != 0:
            
            print("Elements weight should be from 1 to 10 kg")
            element_weight = (float(input("Please add next element weight in kg (0 if there is nothing left):")))

    if element_weight ==0:
        break

    else:
        current_wasted_kg = 20 - current_package_weight
        current_package_weight += element_weight
        packages_kilograms += element_weight

        
        if current_package_weight >= 20:

            packages_number += 1
            current_package_weight = element_weight
            wasted_kilograms += current_wasted_kg
        
            if current_wasted_kg > biggest_waste:

                biggest_waste = current_wasted_kg
           
if current_package_weight > 0:
    packages_number += 1
    current_wasted_kg = 20 - current_package_weight
    wasted_kilograms += current_wasted_kg

    if current_wasted_kg > biggest_waste:
        biggest_waste = current_wasted_kg

                    
print(f'Results:'
    f'\n Number of packages sent:{packages_number}' 
    f'\n Number of kilograms sent:{packages_kilograms}' 
    f'\n Free space wasted in kilograms:{wasted_kilograms}' 
    f'\n Biggest weight waste in one package:{biggest_waste}')