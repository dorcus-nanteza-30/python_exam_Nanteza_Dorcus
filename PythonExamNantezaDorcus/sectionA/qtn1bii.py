# write a python function to sum all the numbers in alist . Hint(apply a loop)
#sample List (9,2,3,5,8)

def sumofListItems():
    numbers = [9,2,3,5,8]
    sum =  0
    
    for number in numbers:
        sum += number
    print("The sum of items in the list is: " + str(sum))
    

sumofListItems()
       