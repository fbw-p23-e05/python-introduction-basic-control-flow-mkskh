num = int(input('Enter number: '))

while num%7==0 and num%2==1 and num>=1:
    print(num, 'is positive, odd and divisible by 7')
    break
else: 
    print('Here is the situation: or number', num, 'is not odd or it is not divisible by 7 or number', num, 'is not positive')