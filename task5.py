num = int(input('Enter number: '))

while num%3==0 and num%2==0:
    print(num, 'is even and divisible by 3')
    break
else: 
    print('Here is the situation: or number', num, 'is not even or it is not divisible by 3')