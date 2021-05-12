names=[]

your_name=input('what is your name: ')

while True:
    input_names=input("enter your colleagues names: ")
    
    if (input_names==''):
        break

    names=names + [input_names]

def greetings(individual_name):
    i=0
    while (i!=len(individual_name)):
        naam=individual_name[i]
        print('hello ' +str(naam))
        i=i+1

greetings(names)

print('thanks for checking my code ' +your_name)
