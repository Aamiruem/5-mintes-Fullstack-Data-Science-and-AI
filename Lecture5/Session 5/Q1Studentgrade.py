marks = int(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("A Grade")

elif marks >= 70 and marks <= 89:
    print("B Grade")

elif marks >= 50 and marks <= 69:
    print("C Grade")

elif marks >= 0 and marks < 50:
    print("Fail")

else:
    print("Invalid marks! Please enter between 0 and 100.")
