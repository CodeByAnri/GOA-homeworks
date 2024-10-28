# 2) for ციკლით მომხარებელს შემოატანინეთ 5 ელემენტი სიაში და დაბეჭდეთ სია

Elements = [input("input any elements you want in the list: " )]
for i in range(1,5):
    Elements.append(input("input any elements you want in the list: " ))
    i += 1
print(Elements)



# 3) შექმენით ხილების სია, 
# სადაც გექნებათ მინიმუმ 3 ელემენტი. 
# მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი, 
# თუ სიის ბოლო ელემენტის ინდექსი არის ლუწი 
# ჩაამატეთ შემოტანილი ხილი სიაში, 
# სხვა შემთხვევაში არ ჩაამატოთ

Fruit_List = ["Apples", "Oranges", "Pineaples"]
Favourite = (input("Enter Your Favourit Fruit: " ))

if len(Fruit_List) % 2 == 1:               #რადგან სიგრძე იზომება 1-დან ხოლო ინდექსუ 0-დან სიგრძე ყოველთვის ერთით მეტია ინდექსის მისამართზე
    Fruit_List.append(Favourite)
print(Fruit_List)



# 4) შექმენით სია შემდგარი სახელებისგან. 
# მომხარებელს შემოატანინეთ მისი სახელი, 
# თუ მისი სახელი იქნება 5 სიმბოლოს ტოლი ან მეტი. 
# ჩაამატეთ სიაში, 
# სხვა შემთხვევაში დაუბეჭდეთ "Name is too short"

Name_List = ["Harry", "Alexa", "Brian", "Putin"]
User_Name = input("Enter Your Name: " )
if len(User_Name) >= 5:
    Name_List.append(User_Name)
else:
    print("Name Is Too Short")
print(Name_List)



# 5) შექმენით სია შემდგარი 10 ელემენტისგან. 
# დაპრინტეთ ის 
# და მომხარებელს შემოატანინეთ რიცხვი 1-დან 10-ჩათვლით. 
# შემდეგ წაშალეთ სიის ის ელემენტი რომელი რიცხვიც გადმოგეცათ 
# და დაპრინტეთ განახლებული სია

Elements = [0, "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
Chosen_Number = int(input("From 1 To 10 Enter The Number You Desire: " ))

if 0 < Chosen_Number <= 10:
    Elements.pop(Chosen_Number - 1)
elif Chosen_Number > 10:
    print("Chosen Number Is Too High It Must Be From 1 To 10")
else:
    print("Chosen Number Is Too Low It Must Be From 1 To 10")
print(Elements)



# 6) კომენტარებით ახსენით რა არის ინდექსი და მოიყვანეთ მაგალითი

# ინდექსი არის მისამართი თუ სად არის შენახული მონაცემი
# მაგალითად იცი რომ ბავშვი უნდა გამოიყვანო სკოლაში ერთ ერთი კლასიდან ამისთვის გჭირდება იმის ცოდნა თუ სად არის შენახული შენი ბავშვი
# პროგრამირებაში მისამართის ანუ ინდექსის ათვლა იწყება 0-დან და რიგით პირველი შენახული მონაცემის მისამართი იქნება "0"
# შესაძლებელია ისიც რომ იყოს ორი ჩამონათვალი და მიუხედავად იმისა რომ მათი მისამართები შეიძლება იყოს იდენტური მთავარი რაც მათ რაობას განსაზღვრავს არის თუ რა არის შენახული ამ ორ განსხვავებულ მაგრამ ინდექსით მსგავს ჩამონათვალში <3