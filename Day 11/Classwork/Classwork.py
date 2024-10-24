# პაროლის ვალიდაციის პროგრამა:
# შექმენით ცვლადი სადაც შეინახავთ პაროლს(მაგალითად: goa1234)
# სანამ მომხარებელი არ შემოიყვანს სწორ პაროლს მანამდე შემოატანინეთ ხელახლა.
# მომხარებელს ექნება 3 ცდა. 
# თუ შემოიყვანა სწორი პაროლი დაუპრინტეთ "წვდომა მიღებულია",
# სხვა შემთხვევაში "სცადეთ ხელახლა",
# დაპრინტეთ რამდენი მცდელობა დარჩა და გამოაკელით ცდას ერთი.
# როდესაც მცდელობები ამოიწურება გათიშეთ while loop-ი



Security_Code = "goa1234"
Enter_Code = input("შეიყვანეთ უსაფრთხოების კოდი: " )
Attempts = 3

while Enter_Code != Security_Code:
    Attempts -= 1
    if Attempts > 0:
        print("Attempts left " + str(Attempts))
        Enter_Code = input("სცადეთ ხელახლა: " )
    else:
        print("თქვენი ექაუნთი დროებით დაბლოკილია სცადეთ მოგვიანებით")
        break
if Enter_Code == Security_Code:
    print("წვდომა მიღებულია")


