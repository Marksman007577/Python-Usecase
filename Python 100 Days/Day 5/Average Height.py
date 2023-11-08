sumOfHeight = 0
totalNumberOfStudent = 0

# Request the student heights
studentHeights = input('Enter the student heights:').split()

for h in range(0, len(studentHeights)):
    studentHeights[h] = int(studentHeights[h])

for i in studentHeights:
    sumOfHeight += i

for n in studentHeights:
    totalNumberOfStudent += 1

averageHeight = round(float(sumOfHeight / len(studentHeights)), 2)

print(f"The average height of the {totalNumberOfStudent} students = {averageHeight}")