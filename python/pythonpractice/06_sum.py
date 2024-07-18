#Create a function that will take two arguments (list, target). 
# Find the two numbers whose sum is equal to the target.

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
target = int(input("Enter the target sum: "))

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if (l1[i] + l1[j]) == target:
            print('{}, {}'.format(l1[i], l1[j]))
