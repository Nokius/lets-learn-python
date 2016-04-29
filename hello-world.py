# This program says Hi and ask for your Name


print('Hi!')
print('What is your name?')   #ask for the name
myName = input()
print('It is nice to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')   #ask for the age
myAge = input()
print('You been  ' + str(int(myAge) - 1) + ' last year.')
