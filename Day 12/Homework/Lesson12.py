# 1) while ციკლის გამოყენებით დაპრინტეთ 1-დან 50-მდე ყველა 4-ის ჯერადი რიცხვის კუბი

num = 1                                                     
while num < 50:     # 1-დან 50-მდე
    if (num % 4) == 0:
        print(str(num ** 3) + " არის 4-ის ჯერადი რიცხვის კუბი")        #4-ის ჯერადი რიცხვის კუბი
    num += 1      # ვუმატებთ 1-ს რათა while ციკლმა ყველა შესაძლო ინტეჯერი განიხილოს და გაჩერდეს რიცხვ 50-ზე



# 2) შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, 
# შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ "Fizz" 
# და გვერდზე მიუწერეთ რიცხვი. 
# თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz" 
# და გვერდზე მიუწერეთ რიცხვი, 
# ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" 
# და გვერდზე მიუწერეთ რიცხვი

for num in range(1, 100):                     # შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე,
    if (num % 3) == 0 and (num % 5) == 0:     # თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" 
        print("FizzBuzz " + str(num))                     
    elif (num % 3) == 0:                      # თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ "Fizz"
        print("Fizz " + str(num))
    elif (num % 5) == 0:                      # თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz"
        print("Buzz " + str(num))



# 3) შექმენით ორი ცვლადი, 
# პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი, 
# მეორეში კი ყველა კენტის. 
# აიყვანეთ ორივე მე-5 ხარისხში 
# და დაპრინტეთ ის, რომელიც არის მეტი

Sum_Of_Even_Numbers = 0         #შექმენით ორი ცვლადი,
Sum_Of_Odd_Numbers = 0
i = 0

while i <= 20:                  # 1-დან 20-ის ჩათვლით
    if (i % 2) == 0:
        Sum_Of_Even_Numbers += i            # პირველში შეინახეთ: ყველა ლუწი რიცხვის ჯამი
    else:                                    
        Sum_Of_Odd_Numbers += i             # მეორეში შეინახეთ: ყველა კენტი რიცხვის ჯამი
    i += 1
Sum_Of_Even_Numbers_5th_Power = Sum_Of_Even_Numbers ** 5    # აიყვანეთ ორივე მე-5 ხარისხში 
Sum_Of_Odd_Numbers_5th_Power = Sum_Of_Odd_Numbers ** 5

if Sum_Of_Even_Numbers_5th_Power > Sum_Of_Odd_Numbers_5th_Power:   # დაპრინტეთ ის, რომელიც არის მეტი
    print("Sum Of Even Numbers To The 5th Power Is Greater")
else:
    print("Sum Of Odd Numbers To The 5th Power Is Greater")



# 4) True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5 <--- გაიგეთ რას გამოიტანს ეს კოდი და ახსენით რატომ.


          # v False v                    v  False  v       v  False v
True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5           # პირველ რიგში ამოვხსნათ and-ოპერაციები 
                                                                                  # მაგრამ პასუხი ისედაც ცხადია რომ არის True
# v True v                                                                        # რადგან ამოცანა იწყება ,,True or" - ით
True or False or False                                                            # რაც არ უნდა იყოს and-ოპერაციის შედეგი
                                                                                  # or-ოპერაციაში თუ ერთ-ერთი მხარე არის True 
# v True v                                                                        # პასუხი აუცილებლად არის True
True or False      # კოდი გამოიტანს True-ს 



# 5) მომხარებელს შემოატანინეთ რიცხვი 
# და გაიგეთ არის თუ არა ის მარტივი, 
# თუ მარტივია დაპრინტეთ "Number is prime", 
# სხვა შემთხვევაში "Number is not prime"
# (მარტივია რიცხვი, რომელიც იყოფა მარტო თავის თავზე და ერთზე)

Number = int(input("Enter A Number And check If Its Prime Or Not: " ))      # მომხარებელს შემოატანინეთ რიცხვი 
Prime_Or_Not = 0

for i in range(1,Number + 1):
    if (Number % i) == 0:   # როდესაც for ციკლი ნახავს i-ს ისეთ მნიშვნელობას რომელიც უნაშთოდ იყოფა number ცვლადზე
        Prime_Or_Not += 1   # Prime_Or_Not ცვლადი გაიზრდება ერთით და საბოლოოდ number-ცვლადის გამყოფების რაოდენობაც დაზუსტდება.
    i += 1

if Prime_Or_Not == 2:     # იმისთვის რომ ციფრი იყოს მარტივი ცვლადი Prime_Or_Not უნდა იყოს 2-ის ტოლი
    print(str(Number) + " Is Prime Number")  # თუ მარტივია დაპრინტეთ "Number is prime" ცოტა დიზაინი შევცვალე 
else:                              # სხვა შემთხვევაში 
    print("Number Is Not Prime")   # "Number is not prime"



# 6) კომენტარებით ახსენით თქვენი თითოეული მოქმედება
