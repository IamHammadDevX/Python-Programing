# BMI CALCULATOR
height = float(input("Enter Height in meters: "));
weight = int(input("Enter Weight in kg: "));

bmiCalc = weight / height**2;
print("Your Body Mass index is: ", int(bmiCalc));