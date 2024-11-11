# 2) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი 
# და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Nika"). 
# გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი

def greet(name):
    print("Hello",  name)
for i   in  range(2):
    name    =   input("Enter Your Name Here: " )
    greet(name)



# 3) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა 2 რიცხვი. 
# ფუნქციამ უნდა დაბეჭდოს ამ რიცხვების ნამრავლი. 
# საბოლოოდ გამოიძახეთ ის.

def multiply(number1,   number2):
    product_of_multiply =   number1 *   number2
    print(product_of_multiply)

number1 =   int(input("Enter    First   Number  Here:   "   ))
number2 =   int(input("Enter    Second  Number  Here:   "   ))
multiply(number1,   number2)



# 4) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სია. 
# ფუნქციამ უნდა დაბეჭდოს ეს სია შებრუნებულად
# (არ გამოიყენოთ slicing-ი)

Reversed_Random_List = []
def  Reversed_list(Random_List):
    for i   in  range(1, len(Random_List) + 1):
        Reversed_Random_List.append(Random_List[-i])
    print(Reversed_Random_List)

Random_List = ["Anri",  "Gio",  "Green",    "Yellow",   "Murderer", "Detective",    12, 10.7]
Reversed_list(Random_List)



# 5) შექმენით ფუნქცია, რომელსაც გადასცემთ რიცხვების სიას. 
# გადაუარეთ გადმოცემულ სიას for ციკლით და დააბრუნეთ ახალი სია, 
# სადაც ჩამატებული იქნება გადმოცემული სიიდან მხოლოდ ის რიცხვები, რომლებიც მეტია 10-ზე. 
# საბოლოოდ დააბრუნეთ ეს სია

changed_Number_List =   []
def changed_list(Number_List):
    for i in range(len(Number_List)):
        if Number_List[i] > 10: changed_Number_List.append(Number_List[i])
    print(changed_Number_List)

Number_List =   [2, 5,  2,  13, 11, 103,    17, 23, 1,  10]
changed_list(Number_List)



# 6) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. 
# ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, 
# გამოიყენეთ slicing-ი

def Chop_Sides(Symbol_List):
    print(Symbol_List[1:-1])

Symbol_List =   [1,   "Anri",   "12",   "Yeah"]
Chop_Sides(Symbol_List)



# 7) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, 
# გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), 
# გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ


def Order_Of_Operations(Num1_List, Num2_List):
    Sum_Of_Num1_List = 0
    Sum_Of_Num2_List = 0
    for i in range(len(Num1_List)):
        Sum_Of_Num1_List += Num1_List[i]
    for i in range(len(Num2_List)):
        Sum_Of_Num2_List += Num2_List[i]
    print(Sum_Of_Num1_List  *   Sum_Of_Num2_List)

Num1_List = [12,    38, 20, 23, 2]
Num2_List = [12,    23, 24, 11, 17, 26, 10, 24, 11, 26, 12, 17, 23, 10]

Order_Of_Operations(Num1_List,  Num2_List)



# 8) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. 
# გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. 
# საბოლოოდ დააბრუნეთ ეს სია.

def Double_It(Num_List):
    Double_Num_List = []
    for i in range(len(Num_List)):
        Num_List[i] *= 2
        Double_Num_List.append(Num_List[i])
    print(Double_Num_List)

Num_List = [12, 23, 24, 11, 17, 26, 10, 24, 11, 26, 12, 17, 23, 10]
Double_It(Num_List)



# 9) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. 
# გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. 
# საბოლოოდ დააბრუნეთ ეს სია

def Even_Nums(Nums):
    Even_Num_List = []
    for i in range(len(Nums)):
        if Nums[i] % 2 == 0:
            Even_Num_List.append(Nums[i])
    print(Even_Num_List)

Nums = [14, 17, 64, 103,    22, 1,  12, 9, 41,  18, 4]
Even_Nums(Nums)



# 10) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. 
# შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, 
# რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია

def First_Letter_N(Names):
    Names_With_First_Letter_N = []
    for i in range(len(Names)):
        Name = Names[i]
        if Name[0] == "N":
            Names_With_First_Letter_N.append(Names[i])
    print(Names_With_First_Letter_N)

Names = ["Nika",    "Anri", "Giorgi",   "Nini", "Lana", "Mariami",  "Nuca", "Nene", "Madona",   "Morisi",   "Nugzari"]
First_Letter_N(Names)