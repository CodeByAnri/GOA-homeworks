# 2) შექმენით სია სადაც გექნებათ რიცხვები. 
# for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი


Numbers = [4, 34, 12, 10, 19, 2]

Highest_Number = Numbers[0]

for i in Numbers:
    if Highest_Number < i:
        Highest_Number = i

print(str(Highest_Number) + " Is The Highest Number In This List")



# 3) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი


Numbers = [4, 14, 12, 10, 9, 2]

for i in range(len(Numbers)):  
    Number = 1
    Factorial = 1
    while Numbers[i] >= Number:
        Factorial *= Number
        Number += 1 
    Numbers[i] = Factorial       

print(Numbers)



# 4) შექმენით სია სადაც გექნებათ რიცხვები. 
# for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი


Numbers = [14, 64, 22, 12, 9, 42]

Lowest_Number = Numbers[0]

for i in Numbers:
    if Lowest_Number > i:
        Lowest_Number = i

print(str(Lowest_Number) + " Is The Lowest Number In This List")



# 5) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, 
# შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).


List_Of_Numbers = [-1, -15, 13, 35, 16, -7, 18, -99]
New_List_Of_Numbers =[]
i = 0

while i < len(List_Of_Numbers):
    if List_Of_Numbers[i] < 0:
        New_List_Of_Numbers.append(List_Of_Numbers[i])
    i += 1
print(New_List_Of_Numbers)



# 6) შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)


List_Of_Numbers = [-1, -15, 13, 35, 16, -7, 18, -99]
Amount = len(List_Of_Numbers)
K = len(List_Of_Numbers)

for Num in range(1, K + 1):
    print(List_Of_Numbers[-Num])



# 7) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება

Characters = ["ye", "ye", "1", "1", "0.2", "0.2",]

No_Duplicates = []

for char in Characters:
    if char not in No_Duplicates:
        No_Duplicates.append(char)
print(No_Duplicates)



# 8) შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის

Str_Var = "Anri"
Opposite_Str_Var = "irnA"



# 9) დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი

Number_input = int(input("Enter The Number Here: " ))
List_Of_Divisors = []

for i in range(1, Number_input + 1):
    if Number_input % i == 0:
        List_Of_Divisors.append(i)
print(List_Of_Divisors)



# 10) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის

Year_input = int(input("Enter The Year: " ))

if (Year_input % 100) > 1:
    Century = Year_input // 100 + 1
else:
    Century = Year_input // 100

print(str(Century) + " Is The Current Century")