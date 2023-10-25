def convert_unit(value, orignal_unit, converted_unit):

    if orignal_unit == "f" and converted_unit == "c":
        ans = (value - 32) / 1.8
        print(f"{value}°F is equal to {ans}°C")

    elif orignal_unit == "c" and converted_unit == "f":
        ans = (value * 1.8) + 32
        print(f"{value}°C is equal to {ans}°F")     

    
    
    elif orignal_unit == "cm" and converted_unit == "m":
        ans = float(value)/100       
        print(f"{value}cm is equal to {ans}m") 
    elif orignal_unit == "mm" and converted_unit == "cm":
        ans = float(value)/10
        print(f"{value}mm is equal to {ans}cm") 
    elif orignal_unit == "m" and converted_unit == "cm":
        ans = float(value)*100
        print(f"{value}m is equal to {ans}cm") 
    elif orignal_unit == "cm" and converted_unit == "mm":
        ans = float(value)*10
        print(f"{value}cm is equal to {ans}mm") 
    elif orignal_unit == "mm" and converted_unit == "m":
        ans = float(value)/1000
        print(f"{value}mm is equal to {ans}m") 
    elif orignal_unit == "m" and converted_unit == "mm":
        ans = float(value)*1000  
        print(f"{value}m is equal to {ans}mm") 
    elif orignal_unit == "km" and converted_unit == "m":
        ans = float(value)*1000
        print(f"{value}km is equal to {ans}m") 
    elif orignal_unit == "m" and converted_unit == "km":
        ans = float(value)/1000
        print(f"{value}m is equal to {ans}km") 
    elif orignal_unit == "mm" and converted_unit == "km":
        ans = float(value)/1000000
        print(f"{value}mm is equal to {ans}km") 
    elif orignal_unit == "cm" and converted_unit == "km":
        ans = float(value)/100000
        print(f"{value}cm is equal to {ans}km") 
    elif orignal_unit == "km" and converted_unit == "cm":
        ans = float(value)*100000
        print(f"{value}km is equal to {ans}mm") 
    elif orignal_unit == "km" and converted_unit == "mm":
        ans = float(value)/1000000
        print(f"{value}km is equal to {ans}mm") 


    elif orignal_unit == "g" and converted_unit == "kg":
        ans = float(value)*1000  
        print(f"{value}g is equal to {ans}kg") 
    elif orignal_unit == "kg" and converted_unit == "g":
        ans = float(value)/1000
        print(f"{value}kg is equal to {ans}g") 
    elif orignal_unit == "mg" and converted_unit == "g":
        ans = float(value)/1000
        print(f"{value}mg is equal to {ans}g") 
    elif orignal_unit == "g" and converted_unit == "p":
        ans = float(value)*0.0004535924
        print(f"{value}g is equal to {ans}pounds") 
    elif orignal_unit == "g" and converted_unit == "mg":
        ans = float(value)/1000
        print(f"{value}g is equal to {ans}mg")
    elif orignal_unit == "p" and converted_unit == "kg":
        ans = float(value)*0.4535924
        print(f"{value}ibs is equal to {ans}g") 
    elif orignal_unit == "kg" and converted_unit == "mg":
        ans = float(value)*1000000
        print(f"{value}kg is equal to {ans}mg")
    elif orignal_unit == "mg" and converted_unit == "kg":
        ans = float(value)/1000000
        print(f"{value}mg is equal to {ans}kg")
    elif orignal_unit == "mg" and converted_unit == "p":
        ans = float(value)/0.0000004535924
        print(f"{value}mg is equal to {ans}ibs")
    elif orignal_unit == "kg" and converted_unit == "p":
        ans = float(value)/0.4535924
        print(f"{value}kg is equal to {ans}ibs")
    elif orignal_unit == "p" and converted_unit == "mg":
        ans = float(value)*0.0000004535924
        print(f"{value}ibs is equal to {ans}mg")
    elif orignal_unit == "p" and converted_unit == "g":
        ans = float(value)*0.0004535924
        print(f"{value}ibs is equal to {ans}g")

    else:
        print("Invalid unit!!")



print("***************************************************")
print("*****______****Unit Converter*****______****")
print("***************************************************\n")

print("what units would you like to print for?")
choice = input("temprature, Length, Weight? ")


if choice == 'temprature':
    
    orignal_unit = input("Enter the unit to convert\n press f or c: ")
    converted_unit = input("Enter the unit to be converted in \n press f or c: ")
    value = int(input(f"Enter the temprature in {orignal_unit}: "))

    convert_unit(value, orignal_unit, converted_unit)


elif choice == 'length':

    orignal_unit = input("Enter the unit for length \n\n press km,cm,mm or m : ")
    converted_unit = input("Enter the unit to be converted in \n\n press km,cm,mm or m: ")
    value = int(input(f"Enter the length in {orignal_unit}: "))

    convert_unit(value, orignal_unit, converted_unit)
elif choice == 'weight':

    orignal_unit = input("Enter the unit to convert \n\n\n press kg,g,mg or p: ")
    converted_unit = input("Enter the unit to be converted in press kg,g,mg or p: ")
    value = float(input(f"Enter the weight in {orignal_unit}: "))

    convert_unit(value, orignal_unit, converted_unit)
  

else:
    ("INVALID!!!!!!!!!")

