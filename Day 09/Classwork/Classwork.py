# while ციკლის საშვალებით გამოიტანეთ რიცხვები 1-იდან 10-მდე

Number = 1
while Number < 11:
    print (Number)
    Number = Number + 1

# while ციკლის საშვალებით გამოიტანეთ რიცხვები 20-იდან 0-მდე

Number2 = 20
while Number2 >= 0:
    print(Number2)
    Number2 = Number2 -1



# while ციკლის საშვალებით გამოიტანეთ 1-დან 20-მდე მხოლოდ ლუწი რიცხვები

Number = 1
while Number < 11:
    print (Number)
    Number = Number + 1


# while ციკლის საშვალებით გამოიტანეთ 1-იდან 100-მდე ყველა 5-ის ჯერადი რიცხვი


Number3 = 5
while Number3 < 100:
    print (Number3)
    Number3 = Number3 + 5


# while ციკლისა და input-ის საშვალებით მომხარებელს შემოატანინეთ პაროლი სანამ არ იქნება ის "goa123"-ის ტოლი

My_password = ("goa123")
password = input("Guess my password: " )
while password != My_password:
    print("wrong")
    password = input("Guess my password: " )
print("Thats Correct!")