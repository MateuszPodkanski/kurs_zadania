elements_number = int(input("Please enter number of elements: ")) 

:
    element_weight = (float(input("Please add next element weight in kg (0 if there is nothing left):")))
    packages_number = 0
    current_package = None
    packages_kilograms = 0
    wasted_kilograms = 0
    biggest_waste = 0

    if element_weight ==0:
        print(f'Results:'
            f'\n Number of packages sent:{packages_number}' 
            f'\n Number of kilograms sent:{packages_kilograms}' 
            f'\n Free space wasted in kilograms:{wasted_kilograms}' 
            f'\n Package with the biggest weight waste: {biggest_waste}')

    
    elif element_weight >10 or element_weight <1:
        print("Package weight should be from 1 to 10 kg")
        continue
    else:
        packages_number +=1
        current_package += element_weight
        if current_package > 20:
            current_package -= current_package
            current_package += element_weight

