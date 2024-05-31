# An input is given as 'n' and you have to check each number upto 'n' and if it is divisible by 3 print Fizz
# if it's divisible by 5 print Buzz and If it is divisible by 3 & 5 then print FizzBuzz

n = 20
list = []
for i in range(1, n+1):
    if i % 15 == 0:
        list.append("FizzBuzz")
    elif i % 3 == 0:
        list.append("Fizz")
    elif i % 5 == 0:
        list.append("Buzz")
    else:
        list.append(i)
        
print(list)