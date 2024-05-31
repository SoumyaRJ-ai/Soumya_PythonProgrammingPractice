# Method - 1
# def sumArray(array):
#     sum = 0
#     for i in array:
#         sum += i
#     return sum

# print(sumArray([2,3,4,5,7]))


# Method - 2
# arr = [2,4,5,6,7,8]
# print(sum(arr))


# Method - 3
from functools import reduce
def sumArrayReduce(array):
    result = reduce(lambda a,b:a+b, array)
    return(result)

print(f"Sum of numbers in the array", sumArrayReduce([2,3,4,5,6,7,8]))