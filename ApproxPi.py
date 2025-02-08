import time

# Approximate Pi using the alternating series
def main():
    realPi = 3.141592653589793

    # Ask user for decimal precision (up to 10)
    precision = int(input("How many decimal points to compute (0 - 10): "))

    if precision < 0 or precision > 10:
        print("Invalid input. Please enter a value between 0 and 10.")
        return

    start = time.time()  

    # Calculate pi using the alternating series
    approximation = 0
    i = 0
    while True:
        term = 4 / (2 * i + 1) * (-1)**i 
        approximation += term
        # Stop when the precision level is reached
        if round(approximation, precision) == round(realPi, precision):
            break
        i += 1

    end = time.time()  # End timing

    elapsedTime = end - start

    print(f"Pi: {round(realPi, precision)}")
    print(f"Calculated in {elapsedTime} seconds.")

if __name__ == '__main__':
    main()
