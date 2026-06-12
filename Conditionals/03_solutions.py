marks = int(input("Enter your average marks :"))


if marks>100:
    print("Invalid input")
    exit()

if marks>89:
    grade = 'A'
elif 79<marks<90:
    grade = 'B'
elif 69<marks<80:
    grade = 'C'
elif 59<marks<70:
    grade = 'D'
else:
    grade = 'F'

print(grade)