heads = 0
tails = 0
number = int(input('Enter the number to flip coin :\n'))

for i in range(0, number):
    import random
    coin = random.randint(0,1)
    if coin < 0.5:
        print("Tails")
        tails = tails+1
    else:
        print("Heads")
        heads = heads+1
HeadsPercentage = heads/number*100
TailsPercentage = tails/number*100
print("Total Percentage of Head ", HeadsPercentage)
print("Total Percentage of Tails ", TailsPercentage)