#Su dung for while
sum = 0
people = int(input("Có bao nhiêu người : "))
# for i in range(0,people):
#     age = int(input(f"Người Thứ #{i+1}: "))
#     if age < 18:
#         price = 25
#     elif age <= 60:
#         price = 100
#     else:
#         price = 50
#     sum = sum + price
# print (f"Total price is: {sum}$")


children = 0
adults = 0
old = 0
if people <= 0:
    print ("Invalid number of people")
for i in range(0,people):
    valid = False #flag
    while not valid:
        age = int(input(f"Người Thứ #{i+1}: "))
        if age < 0:
            print("Invalid age")
        else:
            valid = True

    # if age < 0:
    #     print("Invalid age")
    #     continue
# Sai bởi vì nó chỉ kiểm tra được người đầu tiên trong vòng lặp
    if age < 18:
        children += 1
    elif age <=60:
        adults += 1
    else:
        old += 1
print (f"Total price is: {25*children + 100*adults + 50*old}$")