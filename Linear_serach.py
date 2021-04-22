#LINEAR SEARCH USING FUCTION
#This fuction taking two arguments and no return value
def linear_search(a,num):
    for i in a:
        if(i==num):
            print("Number is found")
            break
        else:
            print("Number is not found")

#taking a list
list=[]
size=int(input("Ente the size of the list:"))

#Insert elements into the list
for i in range(size):                
    no=int(input('Enter number:'))
    list.append(no)                      
print("your list is:",list)

#Enter the number which you want to find
search_no=int(input('Enter the number you want to search:'))
#Calling the fuction and passing two arguments
linear_search(list,search_no)
