# 1) შექმენით სია შემდგარი მინიმუმ 5 ელემენტისგან. წაუშალეთ ამ სიას ბოლო ორი ელემენტი და დაბეჭდეთ ის

Number_List = [4, 13, 15, 16, 12, 10, 7,9, 11, 20]
Number_List = Number_List[0:-2]
print(Number_List)



# 2) შექმენით ცვლადი, სადაც შეინახავთ სთრინგს. slicing-ის მეშვეობით დაბეჭდეთ ის უკუღმა

Var = "String"
print(Var[-1:-len(Var)-1:-1])



# 3) შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან. 
# გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, 
# შემდეგ კი დაბეჭდეთ მათი ჯამი

integer_list = (12, 23, 24, 11, 17, 26, 10, 18, 29, 16)
previous_highest_number = integer_list[0]
previous_lowest_number = integer_list[0]

for i in range(1, len(integer_list)):
    if integer_list[i] > previous_highest_number:
        previous_highest_number = integer_list[i]
    elif integer_list[i] < previous_lowest_number:
        previous_lowest_number = integer_list[i]
print("sum of highest and lowest numbers is " + str(previous_highest_number + previous_lowest_number))



# 4) შექმენით ცვლადი სადაც შეინახავთ სთრინგს და გაიგეთ, არის თუ არა ის პალინდრომი
# (პალინდრომი არის ისეთი სიტყვა, რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)

string = input("please enter a word here: " )

if string == string[-1:-len(string)-1:-1]:
    print("this string is a palindrome")
else:
    print("this word is not palindrome")



# 5) შექმენით რიცხვების სია, გადაუარეთ მას for loop-ით, გაიგეთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში და დაბეჭდეთ მათი რაოდენობა

Number_List = [4, 13, 15, 16, 12, 10, 7,9, 11, 20, 49, 1200, 1]
Odd_number_count = 0
Even_number_count = 0

for index in range(0, len(Number_List)):
    if Number_List[index] % 2 == 1:
        Odd_number_count += 1
    elif Number_List[index] > 0:
        Even_number_count += 1
print("in this list there is " + str(Odd_number_count) + " Odd and " + str(Even_number_count) + " Even Numbers")


# 6) შექმენით სია, სადაც გექნებათ 1-ანები და 0-ანები, 
# შექმენით ახალი სია, რომელიც თავიდან იქნება ცარიელი. 
# for loop-ით გადაუარეთ პირველ სიას და თუ საიტერაციო ცვლადის მნიშვნელობა იქნება 1, ახალ სიაში ჩაამატეთ True, სხვა შემთხვევაში False. 
# საბოლოოდ დაბეჭდეთ ახალი სია

Binary_List = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0,]
Boolean_List = []
for i in Binary_List:
    if i == 1:
        Boolean_List.append(True)
    else:
        Boolean_List.append(False)
print(Boolean_List)