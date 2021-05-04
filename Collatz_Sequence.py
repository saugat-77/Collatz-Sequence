#if the number is even, divide the by two. if the number is odd multiply the number by 3
#and add 1 to the number

guess_number=int(input('input any number: '))
x=0

while(guess_number!=1):
    if(guess_number%2==0):
        (guess_number)=(guess_number)/2
        print('the number becomes: ' + str(int(guess_number)))
        x=x+1

    else:
        guess_number=3*guess_number + 1
        print('the number becomes: ' +str(int(guess_number)))
        x=x+1

print('the proces took '+ str(x) +' steps') 