# 2) შექმენით ცვლადები და შეინახეთ სხვადასხვა მონაცემთა ტიპის მნიშვნელობები.
# შემდეგ შეამოწმეთ თითოეული ცვლადის მონაცემთა ტიპი.

a = "17.5"
b = 17
c = 17.5
d = True
e = False

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))



print("2^^^^^^^^^2")



# 3) მომხარებელს შემოატანინეთ რიცხვი და შეამოწმეთ მისი ტიპი,
# ისე რომ დაგიბრუნდეთ integer

Number = int(input("Enter Number: " ))
print(type(Number))



print("3^^^^^^^^^3")



# 4) გააკეთეთ 5-5 მაგალთი შედარების ოპერატორებზე

a = 15
b = 5
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

a = 5
b = 15
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

a = 50
b = 2
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

a = 2
b = 50
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

a = 13
b = 13
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)



print("4^^^^^^^^^4")



# 5) დაბეჭდეთ ყველა შესაძლო ვარიანტი and და or ოპერატორებზე

a = True
b = True
c = False
d = False

print(a and b)
print(a and c)
print(c and b)
print(c and d)

print(a or b)
print(a or c)
print(c or b)
print(c or d)



print("5^^^^^^^^^5")



# 6) მომხარებელს შემოატანინეთ მისი ასაკი,როგორც სტრინგი და დაბეჭდეთ მისი ტიპი. 
# შემდეგ შეუცვალეთ მას მონაცემთა ტიპი ჯერ integer-ად,
# შემდეგ float-ად (ყოველ გარდაქმნაზე დაბეჭდეთ შედეგი)

Age = str(int(input("Enter Your Age: " )))
print(type(Age))

Age = int(Age)
print(type(Age))
print(Age)

Age = float(Age)
print(type(Age))
print(Age)



print("6^^^^^^^^^6")



# 7) მომხარებელს შემოატანინეთ მისი საყვარელი რიცხვი 
# და გაიგეთ არის თუ არა ის ლუწი

Fav_Number = int(input("Enter Your Favourite Number: " ))
if (Fav_Number % 2) == 0:
    print("This Number Is Even")
else:
    print("This Number Is Odd")



print("7^^^^^^^^^7")



# 8) მომხარებელს შემოატანინეთ მისი ასაკი და სახელი,
# შემდეგ შეამოწმეთ არის თუ არა ის სრულწლოვანი
# და უდრის თუ არა მისი სახელი თქვენს სახელს

My_Name = "Anri"
Your_Name = input("Enter Your Name: " )
Your_Age = int(input("Enter Your Age: " ))

if Your_Age >= 18:
    print("Its True That You Are Adult")
else:
    print("You Aren't Adult")

if Your_Name == My_Name:
    print("It Is True That We Have The Same Name")
else:
    print("We Dont Have The Same Name")



print("8^^^^^^^^^8")
