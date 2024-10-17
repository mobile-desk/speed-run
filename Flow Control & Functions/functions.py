#Return the factorial of the number N
def factorial(N):
    # Your code goes here
    N = int(N)
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N-1)

