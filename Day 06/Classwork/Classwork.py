# 1) მოხარებელს შეეკითხეთ მისი სახელი,
# გვარი
# ასაკი
# და იმეილი,
# შემდეგ კი შემოტანილი მნიშვნელობები დაბეჭდეთ ტერმინალში.
# გამოიყენეთ ეტიკეტი, რომ მიანიშნოთ მომხარებელს თუ რა უნდა შემოიტანოს კონკრეტულ შესაყვან ველში.

Name = input("Enter Your Name: " )                               
Last_Name = input("Enter Your Last Name: " )                     
Age = int(input("Enter Your Age: " ))                            
Gmail = input("Enter Your Gmail: " )                             

print("Individual Named " + Name + " " + Last_Name)             
print("Age is " + str(Age))                                                             
print("His Email is " + Gmail) 



# 2) მომხარებელს შემოატანინეთ ორი რიცხვი და გამოიყენეთ ყველა არითმეტიკული ოპერაცია ამ ორ რიცხვს შორის.

Number1 = int(input("Enter First Number: " ))
Number2 = int(input("Enter Second Number: " ))
print(Number1 + Number2)
print(Number1 - Number2)
print(Number1 / Number2)
print(Number1 * Number2)



# 3) კომენტარებით ახსენით თუ რა არის input-ი და output-ი, ასევე რისთვის გამოიყენება ისინი

# input - არის პროცესი, როდესაც კომპუტერში შედის რაღაც ინფორმაცია.
# output -  არის პროცესი, როდესაც კომპიუტერიდან(ხშირშემთხვევაში input-ის საპასუხოდ) გამოდის რაღაც ინფორმაცია.



# 4) შექმენით კალკულატორის პროგრამა სადაც მომხარებელი შემოიტანს ორ რიცხვს და 4 არითმეტიკული ოპერაციიდან ერთერთს. შეასრულეთ ამ ორ რიცხვს შორის არჩეული არითმეტიკული ოპერაცია


Number1 = int(input("Enter number 1: "))
Number2 = int(input("Enter number 2: "))

operation = input("Enter an operator (+, -, *, /): ")

if operation == "+":
    print(Number1 + Number2)
elif operation == "-":
    print(Number1 - Number2)
elif operation == "*":
    print(Number1 * Number2)
elif operation == "/":
    print(Number1 / Number2)
else:
    print("Invalid operator!")