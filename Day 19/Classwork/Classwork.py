# 1) შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. 
# გადაუარეთ ამ საის while loop-ის გამოყენებით. გაიგეთ ცალკე ლუწი და კენტი რიცხვების ჯამი, საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი



Number_List = [4, 13, 15, 16, 12, 10, 7,9, 11, 20]
number = 0
Sum_Of_Odd = 0
Sum_Of_Even = 0

while number < len(Number_List):
    if number % 2 == 1:
        Sum_Of_Odd += Number_List[number]
    else:
        Sum_Of_Even += Number_List[number]
    number += 1

if Sum_Of_Even > Sum_Of_Odd: print("Sum Of Even Is Greater Than Sum Off Odd And Is Equal to " + str(Sum_Of_Even))
elif Sum_Of_Odd > Sum_Of_Even: print("Sum Of Odd Is Greater Than Sum Off Even And Is Equal to " + str(Sum_Of_Odd))
else: print("Sum of Odds And Sum OF Even Are Same and They Equal to " + str(Sum_Of_Odd))



# 2) შექმენით სიმბოლოების სია, გადაუარეთ მას for loop-ით
# და სიიდან ყველა სიმბოლოს შორის მოახდინეთ კონკადინაცია. 
# ციკლის გარეთ დაგჭირდებათ ცვლადი სადაც შაამატებთ ამ სთრინგებს

Whatever_List =["W", "H", "A", "T", "E", "V", "E", "R"]
for char in Whatever_List:
    Concatenation = Whatever_List[char]
print(Concatenation)
