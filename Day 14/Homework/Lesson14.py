# 6) შექმენით სია სადაც ჩაამატებთ 1-დან 100-მდე ყველა ლუწ რიცხვს. 
# საბოლოოდ დაპრინტეთ ეს სია(გამოიყენეთ for loop)

Numbers_To_Hundred = []

for num in range(1, 100):
    if num % 2 == 0:
        Numbers_To_Hundred.append(num)
    num += 1
print(Numbers_To_Hundred)



# 7) შექმენით სია სადაც ჩაამატებთ ყველა რიცხვს 1-დან 50-ის ჩათვლით. 
# შემდეგ გადაუარეთ for loop-ით 
# და ამ სიიდან წაშალეთ ყველა კენტი რიცხვი. 
# საბოლოოდ დაპრინტეთ მიღებული სია

Numbers_To_Fifty = []

for num in range(1, 50 + 1):
    Numbers_To_Fifty.append(num)
    num += 1
print(Numbers_To_Fifty)

num2 = 49
for num in range(0, 50):
    num += num2
    num2 -= 2
    if Numbers_To_Fifty[num] % 2 == 1:
        Numbers_To_Fifty.pop(num)
print(Numbers_To_Fifty)



# 8) შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი, 
# while loop-ის გამოყენებით წაშალეთ სიის ბოლო ელემენტი იქამდე სანამ სიაში არ დარჩება ორი ელემენტი. 
# ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია

Fruits = ["Banana", "Apples", "Apple", "Banana", "Atemoya", "Avocados", "Blueberry", "Ackee", "Cranberry", "Cantaloupe"]

while len(Fruits) > 2:
    Fruits.pop()
    print(Fruits)



# 9) შექმენით პროგრამა, რომელიც დაითვლის თუ რამდენჯერ შედის სიაში რიცხვი 1 
# numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] 
# (ამისათვის გადაუარეთ სიას for loop-ით)

Numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] 
How_Many_Times = 0

for i in range(len(Numbers)):
    if Numbers[i] == 1:
        How_Many_Times += 1
print("There Are " + str(How_Many_Times) + " Ones in the 'Numbers' List" )



# 10) შექმენით ორი ცარიელი სია, 
# for loop-ის გამოყენებით მომხარებელს 5-ჯერ შემოატანინეთ ნებისმიერი სიტყვა. 
# თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში, 
# სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია

First_List = []
Second_List = []

for i in range(5):
    Word = input("Enter Any Word You Want: " )
    if len(Word) <= 5:
        First_List.append(Word)
    else:
        Second_List.append(Word)
print(First_List)
print(Second_List)