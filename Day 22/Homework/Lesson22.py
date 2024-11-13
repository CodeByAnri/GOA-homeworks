# 2) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა რიცხვი, 
# ხოლო ამ ფუნქციამ უნდა დაბეჭდოს 1-დან გადმოცემულ რიცხვამდე ყველა რიცხვი

def Numbers_Before(Num_input):
    for i in range(Num_input):
        print(i)

Num_input = int(input("Please Enter Desired Number: " ))
Numbers_Before(Num_input)


# 3) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი, 
# ხოლო ამ ფუნქციამ უნდა დააბრუნოს პირველი რიცხვი აყვანილი მე-2 რიცხვის ხარისხში

def Number_PoweredBy(Number, Power):
    result = Number ** Power
    print(result)

Number = int(input("Please Enter Desired Number: " ))
Power = int(input("Please Enter Desired Power: " ))

Number_PoweredBy(Number, Power)