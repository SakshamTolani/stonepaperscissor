import random
lst=['Stone','Paper','Scissors']
i=1
c=0
while i<=10: 
    r=random.choice(lst)
    print('Here are choices: \n Stone \n Paper \n Scissors ')
    user=input('Enter Your choice: ')
    if user in lst:
        if r=='Stone':
            if user=='Scissors':
                print(f'You Lose from {r}')
            elif r==user:
                print('Tie')
            else:
                print(f'You Win from {r}')
                c+=1
        elif r=='Paper':
            if user=='Stone':
                print(f'You Lose from {r}')
            elif r==user:
                print('Tie')
            else:
                print(f'You Win from {r}')
                c+=1
        elif r=='Scissors':
            if user=='Paper':
                print(f'You Lose from {r}')
            elif r==user:
                print('Tie')
            else:
                print(f'You Win from {r}')
                c+=1
        print(f'Please Enter again, you have {10-i} chances left: ')
        i+=1
    else:
        raise Exception('Please Enter Among the options provided:\n 1)Stone \n 2)Paper \n 3)Scissors ')
print(f'Your score was {c} out of 10')
