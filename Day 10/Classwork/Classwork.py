# 1)მომხარებელს შემოატანინეთ მისი ასაკაი,
#  შეინახეთ ის ცვლადში და შეადარეთ.
#  თუ ასაკი არის ლუზი დაბეჭდეთ თქვენი ასაკი არის ლუწი. სხვა შემთხვევაში: თქვენი ასაკი არის კენტი

Age = int(input("Enter Your Age: " ))

if Age % 2 == 0:
    print("Your Age is Even")
else:
    print("Your Age is Odd")


# 2)გამოიტანეთ 10-დან 50-ის ჩათვლით ყველა ლუწი რიცხვი. გამოიყენეთ for loop-ი


for i in range(10,51):
    if i % 2 == 0:
        print(str(i) + " is Even")