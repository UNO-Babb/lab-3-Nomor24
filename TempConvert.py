# TempConvert.py
# Name:
# Date:
# Assignment:

def main():
    # Prompt the user for a Fahrenheit temperature
    tempF = float(input("Enter the temperature in Fahrenheit: "))
    
    # Convert that temperature to Celsius, rounding to 1 decimal precision
    tempC = (tempF - 32) * 5 / 9
    
    # Output the converted temperature
    print(f"{tempF} degrees Fahrenheit is equal to {round(tempC, 1)} degrees Celsius.")

if __name__ == '__main__':
    main()
