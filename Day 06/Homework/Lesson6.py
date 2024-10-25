# 2)კომენტარებით ახსენით რა არის კონკადინაცია და მოიყვანეთ მაგალითები

# კონკოდაცია არის ორი ან მეტი სტრინგის შეერთება ერთმანეთთან
# მაგ: print("An" + "ri" + " " + "Giuna" + "shvili")



# 3)მომხარებელს შემოატანინეთ რიცხვი ერთიდან შვიდამდე,
# შემოტანილი რიცხვის მიხედვით დაპრინტეთ კვირის დღე.
# (მაგალითად მომხარებელმა შემოიტანა 4 >>> "Thursday")

Number = int(input("Choose Number Between 1-7: " ))
if Number == 1:
    print("Monday")
elif Number == 2:
    print("Tuesday")
elif Number == 3:
    print("Wednesday")
elif Number == 4:
    print("Thursday")
elif Number == 5:
    print("Friday")
elif Number == 6:
    print("Saturday")
elif Number == 7:
    print("Sunday")
else:
    print("Invalid Date")



# 4)მომხარებელს შემოატანინეთ ორი რიცხვი,
# შეინახეთ ორივე ცვლადში.
# მოახდინეთ მათ შორის შედარება
# და შედეგი(True or False) გამოიტანეთ ტერმინალში

Number1 = int(input("Choose 1st Number: " ))
Number2 = int(input("Choose 2nd Number: " ))

if Number1 > Number2 :
    print("True")
else:
    print("False")



# 5)მომხარებელს შემოატანინეთ თავისი ასაკი,
# თუ ის არის 18 წლის ან ზემოთ დაპრინტეთ "You are adult",
# სხვა შემთხვევაში დაპრინტეთ "You are kid"

Age = int(input("Enter Your Age: " ))

if Age >= 18 :
    print("You Are Adult")
else:
    print("You Are Kid")



# 6)მომხარებელს შემოატანინეთ 4 რიცხვი.
# შეინახეთ ისინი ცვლადებში
# და დაბეჭდეთ მათი საშუალო არითმეტიკული

Number1 = int(input("Enter 1st Number: " ))
Number2 = int(input("Enter 2nd Number: " ))
Number3 = int(input("Enter 3rd Number: " ))
Number4 = int(input("Enter 4th Number: " ))
Arithmetic_Mean_Of_Numbers = (Number1 + Number2 + Number3 + Number4) / 4
print(Arithmetic_Mean_Of_Numbers)



# 7)გააკეთეთ 3-3 მაგალითი int() და str() ფუნქციებზე

print(7000 - 4994)
print(int("7000") - 4994)
print(int("7000") - int("4994"))

print("Anri" + "Giunashvili" + "2006" + "@gmail.com")
print("Anri" + "Giunashvili" + str(2006) + "@gmail.com")
print("Anri" + "Giunashvili" + str(2000 + 5000 - 4994) + "@gmail.com")