classes = []

total = int(input('How many classes are you taking this semester ?: '))

for i in range(total):


 one = input('Enter the name of the class: ')
 classes.append(one)

print('The classes you are taking are: ')

for one in classes:

 print(one)