# 1) შექმენით ფუნქცია სახელად add რომელსაც გამოძახებისას ფრჩხილებში გადასცემთ ორ რიცხვს, 
# ამ ფუნქციამ კი უნდა გააკეთოს არითმეტიკული ოპერაცია, კონკრეტულად შეკრება, 
# მიღებული შედეგი კი უნდა დააბრუნოს ფუნქციამ, დაბრუნებული მნიშვნელობა შეინახეთ ცვლადში


def add(number1, number2):
    sum = number1 + number2
    print(sum)

number1 = int(input("Enter First Number Here: " ))
number2 = int(input("Enter Second Number Here: "))

add(number1, number2)