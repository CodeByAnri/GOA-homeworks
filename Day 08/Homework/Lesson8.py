# 2)გამოიტანეთ თქვენი სახელი და გვარი იმდენჯერ, რამდენი წლისაც ხართ

My_identity = "Anri Giunashvili"

for i in range(18):
    print(My_identity)



print("4^^^^^^^^^^4")



# 3)გამოიტანეთ ტერმინალში რიცხვები 1-დან 20-ის ჩათვლით

for i in range(20):
    print(i + 1)



print("3^^^^^^^^^^3")



# 4)გამოიტანეთ ტერმინალში რიცხვები 20-დან 0-მდე

for i in range(20):
    print(i + (20 - 2 * i))



print("4^^^^^^^^^^4")




# 5)გამოითვალეთ 1-დან 50-ის ჩათვლით ყველა რიცხვის ჯამი და დაპრინტეთ საბოლოო შედეგი

Final_Outcome = 0
for i in range(51):     # range(51) - ათვლა იწყება 0-დან და გვჭირდება 50-ის ჩათვლით ყველა რიცხვი 
    Final_Outcome = Final_Outcome + i
print (Final_Outcome)



print("5^^^^^^^^^^5")



# 6)დაბეჭდეთ 1-დან 5-ის ჩათვლით რიცხვთა კვადრატი(n * n)

for i in range(6):      # range(6) - ათვლა იწყება 0-დან და გვჭირდება 5-ის ჩათვლით ყველა რიცხვი 
    print(i * i)



print("6^^^^^^^^^^6")



# 7)დაბეჭდეთ ყველა ლუწი რიცხვის ჯამი 1-დან 10-ის ჩათვლით

Total_Even_Numbers = 0
for i in range(11):      # range(11) - ათვლა იწყება 0-დან და გვჭირდება 10-ის ჩათვლით ყველა ლუწი რიცხვი 
    if i % 2 == 0:
        Total_Even_Numbers = Total_Even_Numbers + i
print(Total_Even_Numbers)



print("7^^^^^^^^^^7")



# 8)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ცვლადში,
# შემდეგ კი 0-დან შემოტანილი რიცხვის ჩათვლით შეამოწმეთ, თუ ლუწია დაბეჭდეთ რიცხვი is Even,
# სხვა შემთხვევაში რიცხვი is Odd;(მაგალითად 4, ლუწია ამიტომაც დაბეჭდავთ "4 is Even")

Number = int(input("Enter A Number: " ))
for i in range(Number + 1):
    if (i % 2) == 0:
        print(str(i) + " is Even")
    else:
        print(str(i) + " is Odd")



print("8^^^^^^^^^^8")