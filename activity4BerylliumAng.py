#Ang,Beryllium

#Code 1
    #A. The output would be p, because the 5th letter of the name is p
    #B. The output would be an index order, because the nChar exceeds the amount of letters in the name
    #C I would add a line of code that checks if nChar is longer than the length of the name, and if nChar is longer, we will subtract the length of the name from nChar for no error message.


#Code 2
    #A. The for loop is missing a colon, I added a colon for the code to work.
    #B I subtracted i from nChar during the for loop so it makes the name look like an inverted triangle.

#Code 3
#The funjction to add all squared numbers is:
n = 0
while n < 1 or n > 100:
    n = input("Enter a number from 1 to 100 : ")
    n = int(n)

def sum_of_squared(n):
    number = 0
    for i in range(n+1):
        i = (i*i)
        number = i+number
    print(f"{number}")

sum_of_squared(n)
