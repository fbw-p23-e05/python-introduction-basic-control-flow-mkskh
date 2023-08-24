num = int(input('Enter number: '))

for i in range(2, num+1): 
    if num%i == 0:
        print(i)

# if we want to get result without '1' then we need to write (2, num+1) (how in example of task), if we want to get result with '1', then we need to write (1, num+1)