# 2) შექმენით პროგრამა while ციკლის საშვალებით რომელიც გამოთვლის ყველა ნატურალური რიცხვის ჯამს 1-იდან 50-მდე

Prev_Number = 0
Sum_Of_Numbers = 0
Raise_Number = 0

while Raise_Number < 50:
    Raise_Number += 1
    Sum_Of_Numbers = Prev_Number + Raise_Number
    Prev_Number = Sum_Of_Numbers
    print(Sum_Of_Numbers)



# 3) შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) მანამდე სანამ არ შეიყვანს 1234-ს

Correct_PIN = 1234
PIN = int(input("Guess The Correct Pin: " ))

if PIN < 1000 or PIN > 9999:
    print("Incorrect PIN Make Sure You Are Trying To Guess 4 Digit Pin")
elif PIN == 1234:
    print("You Guessed It! Thats Mighty Impressive HAHA!")
else:
    print("Thats Wrong Unfortunately.. You Aren't Planning To Give Up Now Are You>?!")



# 4) შექმნით რიცხვის გამოცნობის თამაში while ციკლით,
# რომელიც მომხმარებელს შეეკითხება რიცხვს 1-დან 10-მდე, 
# სანამ მომხმარებელი არ შეიყვანს თქვენთვის სასურველ რიცხვს

Chosen_Number = 7
Choose_Number = int(input("Guess The Chosen Number: " ))

while Choose_Number != Chosen_Number:
        if Choose_Number < 1 or Choose_Number > 9:
             print("Invalid Number Make Sure You Are Trying To Guess Numbers From 1 To 10")
        print("Thats Incorrect.. Try Agin")
        Choose_Number = int(input("Guess The Chosen Number: " ))

print("Nice You've Guessed It!!")



# 5) ტექსტურ ფაილში ახსენით როდის ვიყენებთ while ციკლს და როდის for ციკლს.

# While - ეს ციკლი მოსახერხებელია იმ შემთხვევებისთვის როდესაც არ არის ცნობილი ზუსტად რომელი მოქმედებისას მივიღებთ საჭირო მონაცემს..
# For - ციკლი გამოიყენება იმ შემთხვევებში როცა ნათლად ჩანს რამდენი გამეორებაა საჭირო საჭირო მონაცემის მისაღებად..