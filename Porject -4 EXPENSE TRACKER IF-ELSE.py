month=input("Enter the Monthe Name: ")
Expense=input("Enter the Expense Categories: ")
price=int(input("Enter the Item Price: "))
a=True
total=0
i=0
total=total+price
i+=1
d={}
d[i]={
    Expense:price
}
while a:
    Reenter=input("Enter the Answer Yes or No: ")

    if Reenter=='Yes' or Reenter=='yes':
        Expense=input("Enter the Expense Categories: ") 
        price=int(input("Enter the Item Price: "))
        total=total+price
        i+=1
        d[i]={
            Expense:price
        }
       
        
    elif Reenter=='No' or Reenter=='no':
        a=False


if d:
    for key,value in d.items():
        print(f"Item and Price - {key}:{value}")
        print(f"Total Price: {total}")

# month=input("Enter the Monthe Name: ")
# Expense=input("Enter the Expense Categories: ")
# price=int(input("Enter the Item Price: "))
# a=True
# total=0
# i=0
# total=total+price
# i+=1
# print(i)
# d={}
# d[i]={
#                 Expense:price
# }
# while a:
#     # print(i)
#     choose=input("Enter the Answer Yes or No: ")
#     match choose:
#         case 'Yes':
#             Expense=input("Enter the Expense Categories: ")
#             price=int(input("Enter the Item Price: "))
#             total=total+price
#             i+=1
#             d[i]={
#                 Expense:price
#             }
#             print(i)
#         case 'No':
#             a=False
#         case _:
#             print("Default Case Run..")
# print(total)
# if d:
#     for key,value in d.items():
#         print(f"Item and Price - {key}:{value}")
        


