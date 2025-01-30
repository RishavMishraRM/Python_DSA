# Head Recursion

def calculate(n):
    if n > 0:
        calculate(n-1)
        k = n ** 2
        print(k)

calculate(4)

# Output:
# 1
# 4
# 9
# 16