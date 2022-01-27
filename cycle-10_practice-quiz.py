# Author: SMR (AMDG) 01/27/22

#  Defined first function
def food_costs(groceries,costs):
    groceries_mod = groceries
    x=0
    for i,v in enumerate(groceries):
        x+=1
    return groceries_mod

print(food_costs([['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt',]],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == 
['apple: $1.99','pear: $2.99','banana: $0.99',],['salmon: $9.99','tuna: $10.99','cod:$6.99',],['milk: $3.49','eggs: $2.49','yogurt: $1.49',])
# Ran out of time to fix the errors in the list.



# Question 2:
# Input Statement
number = int(input("Enter a number:")) 
# Count
check = 1 
# For Loop
for index in range(2, number+1): 
    check *= index
# Final Print Statement
print("The factorial of {} is: {}".format(number, check))

# Question 3:
def Fib(n):
# If n is zero return as zero
    if n == 0:
        return 0
# If N is less than 0 tell user to input again
    elif n<0:
        print("Incorrect input")
 
# Check if n is 1 or 2. This will fix the repeat of 1 in the beginnign of the Fibonacci sequence.
    elif n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

print(Fib(3))
# Didnt have enough time to fix to make it return as a full list, rather than just the answer.