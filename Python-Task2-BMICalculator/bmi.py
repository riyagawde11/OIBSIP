def calculate_bmi():
    print("--- Welcome to BMI Calculator ---")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obesity")
            
    except ValueError:
        print("Invalid input! Please enter numbers for weight and height.")

if __name__ == "__main__":
    calculate_bmi()