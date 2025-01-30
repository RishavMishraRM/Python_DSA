# Tail Recursion

def calculate(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate(n-1)

calculate(4)

# Output:
# 16
# 9
# 4
# 1
