def numrecursive(n, basenumber=8, common_difference=7):
    if n == 1:
        return basenumber
    else:
        return numrecursive(n - 1, basenumber + common_difference, common_difference)

# Test the function with examples
print(numrecursive(1))   # Output: 8
print(numrecursive(5))   # Output: 36
print(numrecursive(10))  # Output: 71
