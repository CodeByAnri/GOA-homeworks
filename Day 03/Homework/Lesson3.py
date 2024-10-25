# 2) https://www.w3schools.com/python/python_variables.asp 
# გადახედეთ ამ რესურს თავიდან ბოლომდე და დაწერეთ ცვალდების შესახებ 10 მაგალით

x = 17     # ცვლადს მივანიჭეთ მნიშვნელობა
y = 3        
print(x)
print(y)


x = 13    
x = "Anri Giunashvili"     # ცვლადს შევუცვალეთ მნიშვნელობა
print(x)


x = str(7)     # x will be '7'
y = int(7)     # y will be 7
z = float(7)   # z will be 7.0


x = 91251
y = "Anri Giunashvili" 
print(type(x))   # კონკრეტული ცვლადის ტიპის გარკვევა 
print(type(y))   # როგორიცაა str, int და float


x = "Anri"
# "Anri" და 'Anri' ერთმანეთის იდენტურია
x = 'Anri'


Hourly_Payment = 5
Hours_Worked = 17
Total_Salary = Hourly_Payment * Hours_Worked
print(Total_Salary)



# 3) კომენტარებით აღზერე ცვლადის შექმნის თითოეული ნაბიჯი(სულ 3).

# Step1: შევარჩიოთ ისეთი ცვლადი რომელიც რელევანტურია იმ ინფორმაციის რომლის მნიშვნელობის მინიჭებასაც ვუპირებთ ცვლადს.
# Step2: ცვლადის შერჩევის შემდგომ გამოვიყენოთ მნიშვნელობის მიმნიჭებელი ოპერაცია "=".
# Step3: მივანიჭოთ ცვლადს მნიშვნელობა.
# Example: Variable = Value



# 4) შექმენით სამი ცვლადი num1, num2 და num3, შემდეგ კი დაპრინტეთ მათი ჯამი

num1 = 15
num2 = 17
num3 = 3
print(num1 + num2 + num3)



# 5) შექმენით ორი ცვლადი x, y და დაპრინტეთ მათი ნამრავლი.

x = 31
y = 3
print(x * y)



# 6) მართკუთხედის პერიმეტრი:
# შექმენით ორი ცვლადი length და width(მართკუთხედის გვერდები),
# მიანიჭეთ მნიშვნელობებად 20 და 10. 
# გამოითვალეთ მართკუთხედის პერიმეტრი და დაპრინტეთ.

length = 20
width = 10
Rectangle_Perimeter = 2 * (length + width)
print(Rectangle_Perimeter)



# 7) შექმენით სამი ცვლადი age1, age2, age3, სადაც შეინახავთ თქვენი და ოჯახის წევრების ასაკს. 
# გაიგეთ ცვლადებში შენახული მნიშვნელობების საშუალო არითმეტიკული და დაპრინტეთ.

age1 = 16
age2 = 18
age3 = 41
Arithmetic_Average_Age = (age1 + age2 + age3) / 3
print(Arithmetic_Average_Age)



# 8) შექმენით ორი ცვლადი,
# პირველში შეინახეთ თქვენი სახელი, 
# მეორეში გვარი. 
# მოახდინეთ კონკადინაცია(რესურსებში არის ჩაგდებული და გადახედეთ) ამ ორ ცვლადს შორის და პასუხი შეინახეთ ახალ ცვლადში სახელად result. 
# დაბეჭდეთ result ცვლადი.

Name = "Anri"
Lastname = "Giunashvili"
Result = Name + " " + Lastname
print(Result)



# 9) შექმენით ორი ცვლადი age და fullname, 
# პირველში შეინახეთ თქვენი ასაკი, 
# ხოლო მეორეში სრული სახელი(სახელი და გვარი). 
# დაბეჭდეთ fullname ცვლადში შენახული მნიშვნელობა იმდენჯერ, რამდენი წლისაც ხართ(გამოიყენე შექმნილი age ცვლადი). 
# დაბეჭდე ერთი print()-ფუნქციის მეშვეობით

age = 18
fullname = "Anri Giunashvili"
print(age * (fullname + "; "))



# 10) კომენტარებით დაწერე, თუ რა არის დეკლარაცია, ინიციალიზიება და რეინიციალიზება. 
# ახსენი რა განსხვავებაა ამათ შორის 
# და მოიყვანე თითოეულზე 2-2 მაგალითი

# Declaration - რაიმე მნიშვნელობისთვის(Value) ახალი ცვლადის(Variable) შექმნა პროგრამაში, რათა მოწყობილობას(Device) მივაწოდო ინფორმაცია ზოგადი სახით.
# მაგალითად: ვიცი რომ ვარ 18 წლის და მჭირდება ცვლადის(Variable) შექმნა, როგორიცაა Age ან ვიმყოფები საქართველოში(Georgia) და მჭირდება ცვლადი(Variable), როგორიცაა Location მოწყობილობისთვის(Device) ინფორმაციის მისაწოდებლად.

Age = 18
Location = "Georgia"

# Initialisation - ცვლადისთვის მნიშვნელობის(Value) მინიჭება, რათა ცვლადის(Variable) გამოძახებისას მოწყობილობამ(Device) შეასრულოს ინიციალიზაციით გადაცემული ბრძანება.
# მაგალითად: მოწყობილობა(Device) ფლობს ინფორმაციას ცვლადი(Variable) Age-ს დახმარებით, რომ მე გამაჩნია ასაკი მაგრამ არიცის რამდენი წლის ვარ.. გვჭირდება ინიციალიზაცია რათა გაიგოს რომ 18 წლის ვარ,
# ან იცის რომ სადღაც ვარ. ცვლადი(Variable) Location-ის დახმარებით მაგრამ არიცის რომ ვარ საქართველოში(Georgia).. ამ დროს მჭირდება ინიციალიზაცია რათა გავაგებინო სად ვარ.

Age = 18
Location = "Georgia"

# Reinitialization - ცვლადის მნიშვნელობის(Value) ცვლილება.
# მაგალითად აქამდე იცოდა რომ ვიყავი 18 წლის.. გავიზარდე და გავხდი 19-ის ან თუნდაც ვიყავი საქართველოში(Georgia) და ახლა ვიმყოფები ავსტრალიაში(Australia)

Age = 18                 # იმ შემთხვევაში თუ ცვლადს(Variable) გამოვიძახებთ რეინიციალიზაციამდე, ცვლადის(Variable) ადრინდელი მნიშვნელობა(Value) იქნება მოქმედი.
Location = "Georgia"
Age = 19                 # თუ ცვლადს(Variable) რეინიციალიზაციის შემდგომ გამოვიძახებთ, ცვლადის(Variable) ახალი მნიშვნელობა(Value) დაიწყრბს მოქმედებას.
Location = "Australia"   