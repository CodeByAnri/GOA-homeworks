# 2) მომხარებელს შემოატანინეთ რიცხვი
# და დაბეჭდეთ, რამდენჯერ შედის შემოტანილი რიცხვი 100-ში.
# გააკეთეთ ყველაზე მოკლე გზით(ამისათვის გამოიყენეთ გაყოფის სწორი ტიპი)

Pick_A_Number = int(input("Enter Your Chosen Number: " ))
print(str(100 // Pick_A_Number) + " Times In A Hundred")



# 3) while ციკლის გამოყენებით გამოიტანეთ 1-დან 20-მდე ყველა კენტი რიცხვის ჯამი

i = 1
Prev_i = 0
while i < 20:
    if (i % 2) == 1:
        Prev_i += i
    i += 1
print(str(Prev_i) + " Is The Sum Of All The Odd Numbers")



# 4)მომხარებელს შემოატანინეთ ორი რიცხვი
# და დაბეჭდეთ ის, რომელიც არის მეტი. 
# თუ ორივე რიცხვი ტოლია დაბეჭდეთ "Both numbers are equal"

Chosen_Number1 = int(input("Enter First Chosen Number: " ))
Chosen_Number2 = int(input("Enter Second Chosen Number: " ))

if Chosen_Number1 > Chosen_Number2:
    print(str(Chosen_Number1) + " Is Greater Than The Other")
elif Chosen_Number1 < Chosen_Number2:
    print(str(Chosen_Number2) + " Is Greater Than The Other")
else:
    print("Both Numbers Are Equal")



# 5)მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ შემოტანილი რიცხვის ფაქტორიალი(დასერჩეთ რა არის ფაქტორიალი)

Factorial_Of_A_Number = int(input("Factorial Of Which Number Do You Seek: " ))
Prev_i = 1
for i in range(1,Factorial_Of_A_Number + 1):
    i = i * Prev_i
    Prev_i = i
print(i)

# 6)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. 
# შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი

Square_Of_A_Number = int(input("Enter The Number From 1 TO Which You Want The Sum Of Squears Of: " ))
Prev_i = 0
Sum_Of_Squeares = 0
for i in range(1, Square_Of_A_Number + 1):
    Prev_i = i
    i = Prev_i * i
    Sum_Of_Squeares += i
print(str(Sum_Of_Squeares) + " Is The Sum Of Squears From 1 To Your Chosen Number")



# 7)თამაში "რიცხვის გამოცნობა". 
# შექმენით ცვლადი და შეინახეთ რომელიმე რიცხვი 1-დან 20-ის ჩათვლით(ეს იქნება ჩაფიქრებული რიცხვი).
# გამოიყენეთ while loop-ი და მომხარებელს შემოატანინეთ რიცხვი იქამდე სანამ არ გამოიცნობს მას.
# თუ მომხარებლის მიერ შემოტანილი რიცხვი მეტია ჩაფიქრებულზე, დაპრინტეთ Too high, 
# თუ ნაკლებია Too low, 
# ხოლო იმ შემთხვევაში თუ მომხარებელი გამოიცნობს რიცხვს დაპრინტეთ "You win"

Chosen_Number = 13
Guess_Number = int
while Guess_Number != Chosen_Number:
    Guess_Number = int(input("Guess The Number: " ))
    if Guess_Number < Chosen_Number:
        print("Too Low")
    elif Guess_Number > Chosen_Number:
        print("Too High")

print(str(Guess_Number) + " Was Correct You Win")