def temp():
    print("From Which to Convert the Temperature..")
    print("Option 1. Fahrenheit to Celsius")
    print("Option 2. Celsius to Fahrenheit")
    option = int(input("Enter your Option : "))
    if option == 1:
        f = float(input("Enter Your Current Temperature : "))
        r = (f-32) * 5/9
        print(f"Your Convertable Temperature is in Celsius : {r}")
    else:
        c = float(input("Enter Your Current Temperature is : "))
        o = (9/5)*c+32
        print(f"Your Convertable Temperature is in Fahrenheit : {o}")
        
    
temp()
