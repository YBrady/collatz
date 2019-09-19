# The number we will perform the collatz operations on
n = 20

# Keep looping until we reach 1
# Note: this assumes the collatz conjecture is true
while n != 1:
    # Print the current value of n
    print (n)
    # Check if n is even
    if n % 2 == 0:
        # If n is even divide by 2
        n = n/2
    else:
        # If n is odd, multiply by 3 and add 1
        n = (n*3)+1
# Finally print the 1
print(n)