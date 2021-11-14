#Roberto Roman
#11-13-2021

#Problem 4
# Write a Python function that takes a list of numbers and returns a new list with
# unique elements of the first list.
# Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the appendfunction.
#Local Variable Function
def uniquel (alist):
    unique_list = []
    #Doing loop
    for num in alist:
        if num  not in unique_list:
            unique_list.append(num)
        #Stopping loop
        return unique_list
#We are calling the variable to be executed
print (uniquel([1,3,3,3,6,2,3,5]))