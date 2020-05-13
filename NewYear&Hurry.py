n,k = list(map(int,input().split()))
timeLeft = 240-k
timeConsumed = 5
problemNumber = 2
numberOfProblemsSolved = 0
while timeConsumed <= timeLeft and n>=1:
    timeConsumed+= 5 * problemNumber
    problemNumber+=1
    n-=1
    numberOfProblemsSolved+=1
print(numberOfProblemsSolved)