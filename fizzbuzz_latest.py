def fizzbuzz(list1):
    for index, value in enumerate(list1):
        if value % 3 == 0 and value % 5 == 0 :
            list1[index] = "FizzBuzz"
        elif value % 3 == 0:
            list1[index] = "Fizz"
        elif value % 5 == 0:
            list1[index] = "Buzz"
    return list1
            
list1 = [3, 4, 5, 10, 9, 15, 30, 6, 15] 
print(fizzbuzz(list1))
