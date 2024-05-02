# write a python program to convert temperatures from celsius and fahrenheit
#formulae F =(9/5c+32)

def temperatureConvertions():
    
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    
    option = int(input("Select your choice (1 or 2): "))
    
    if option == 1:
        celsius = float(input("Enter temperature in celsius Degrees: "))
        fahrenheit = (9/5 * celsius) + 32
        print (f"{celsius} C is equal to {fahrenheit} F")
    
    elif option == 2:
        fahrenheit = float(input("Enter temperature in fahrenheit Degrees: "))
        celsius = (5/9 * fahrenheit - 32 )
        print (f"{fahrenheit} F is equal to {celsius} C")
    
    else:
        print("Invalid Option!")
        
temperatureConvertions()