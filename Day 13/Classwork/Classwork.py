# 1) შექმენით სია, რომელსაც შეინახავთ ცვლადში სახელად friends. 
# მაგ სიაში უნდა შეინახოთ მინიმუმ 5 მეგობრის სახელი.
# პირველ რიგში გამოიტანეთ თქვენი საუკეთესო მეგობრის სახელი ინდექსების დახმარებით. 
# დაბეჭდეთ სია. 
# შეცვლაეთ მე-3 ინდექსზე მყოფი სახელი ახალით 
# და დაბეჭდეთ სია. 
# აბოლოოდ დაბეჭდეთ მთლიანი სიის სიგრძე

Friends = ["Alex", "Brian", "Lucas", "Mary", "Sara"]
Bestfriend = Friends[0]
print(Bestfriend)
print(Friends)

Friends[3] = "Nika"
print(Friends)
print(len(Friends))




# 2) შექმენით მანქანების სია, სადაც გამოიყენებთ ერთ-ერთ ფუნქციას, რომ სიაში დაამატოთ ახალი მანქანა.

Cars = ["Bugatti", "BMW", "Mercedes", input("Enter The Car You Want To Add: " )]


# 3) შექმენით რიცხვების სია სადაც გექნებათ მინიმუმ ხუთი რიცხვი. 
# შეცვლაეთ ამ სიის პირველი ელემენტი 
# და გაუტოლეთ ის 50-ს. 
# შემდეგ კი გამოიტანეთ სიიდან პირველი და ბოლო რიცხვის ჯამი

Numbers =  [2, 5, 6, 8, 10]
Numbers[0] = 50
print(Numbers[0] + Numbers[4])


