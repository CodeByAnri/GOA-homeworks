# 2)  შექმენით string-ების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ სიაში არსებული ყველა სიტყვის სიმბოლოთა რაოდენობა

String_List = ["Cha", "Ting", "All", "Day", "So", "Bor", "ing"]

for string in range(len(String_List)):
    print(len(String_List[string]))



# 3) შექმენით რიცხვების სია, while loop-ის გამოყენებით გაიგეთ ამ სიაში ყველა ლუწი რიცხვის ჯამი და დაპრინტეთ

Integer_List = (12, 23, 24, 11, 17, 26, 10)
Sum = 0

for integer in range(len(Integer_List)):
    if Integer_List[integer] % 2 == 0:
        Sum += Integer_List[integer]
print(Sum)



# 4) შექმენით სახელების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე

Name_List = ["Anri", "Nika", "Luka", "Alex", "Adrian", "Rezo", "Tedo", "Lana", "Mari", "Andria"]

for Name in range(len(Name_List)):
    Detector = Name_List[Name]
    if Detector[0] == "A":
        print(Detector)



# 5) შექმენით რიცხვების სია, სადაც გექნებათ დუბლიკატები. გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი რცხვების ჯამი, რომლებიც არ მეორდება სიაში

Integer_List = (12, 23, 24, 11, 17, 26, 10, 24, 11, 26, 12, 17, 23, 10)
integer = 0

No_Duplicates = []

for integer in Integer_List:
    if integer not in No_Duplicates:
        No_Duplicates.append(integer)
print(No_Duplicates)



# 6) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა მარტივ რიცხვს

User_input = int(input("Enter The Number Here: " ))
Diviser = 1

while Diviser <= User_input:
    Times_Divided = 0
    for Divider in range (1, Diviser + 1):
        if Diviser % Divider == 0:
            Times_Divided += 1
    if Times_Divided == 2:
        print(Diviser)
    Diviser += 1



# 7) შექმენით სია შემდგარი 5 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ მე-3 და მე-4 ელემენტები

Just_A_List = ["Whatever", "Not", "Like", "I", "Care"]
print(Just_A_List[2:4])



# 8) შექმენით რიცხვების სია, შემდგარი 10 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ სიის ყოველი მეორე ელემენტი

Just_A_List = ["Whatever", "Not", "Like", "I", "Care", 12, 23, 24, 11, 17]
print(Just_A_List[1:10:2])



# 9) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ სთრინგის ბოლო სამი სიმბოლო(გამოიყენეთ slicing და მინუსიანი ინდექსები)

Variable = "String"
print(Variable[-3:])



# 10) შექმენით რიცხვების სია, დაბეჭდეთ სია თავიდან ბოლომდე slicing-ის გამოყენებით

Integer_List = (12, 23, 24, 11, 17, 26, 10, 24, 11, 26, 12, 17, 23, 10)
print(Integer_List[:])