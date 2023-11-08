highestScore = 0

# Request the student scores
studentScores = input('Enter the student scores:').split()

for s in range(0, len(studentScores)):
    studentScores[s] = int(studentScores[s])


for i in studentScores:
    if i > highestScore:
        highestScore = i


print(f'The highest score in the class is: {highestScore}')