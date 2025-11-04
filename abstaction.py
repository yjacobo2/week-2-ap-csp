# abstraction is when I hide
# the complex details for something
# alot more simple.

#personal information
# a functyion allows us to wrap up data or
#information into a special box or
#enclosure for reuse
# define a function
def personinformation():
    question1 = input("how old are you?")
    question2 = input("where do you live?")
    question3 = input("what school do you go to?")
    print(question1 + question2 + question3)

#call the function
personinformation()
personinformation()
personinformation()

# make a function that guesses how old you are?
def ageandbirth():
    q1 = int(input("when were you born?"))
    q2 = int(input("what year were you born?"))
    answer = q1 - q2
    result = print(f' you are {answer} years old')

#call the function
ageandbirth()
ageandbirth()
ageandbirth()

#git add .
# git commit -m "abstraction"
#git push origin
# if you get an error
#git push origin -- force
