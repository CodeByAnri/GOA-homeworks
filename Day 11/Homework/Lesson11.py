# # 1) გააიაზრეთ ეს კოდი, დაკომენტარეთ თითოეული კოდი

# secret_pass = "luka1234"    # უსაფრთხოების კოდი / პაროლი / საიდუმლო გასაღები
# user_pass = ''              # მომხმარებლის შეყვანილი კოდი / პაროლი / საიდუმლო გასაღები 

# tries = 3

# while tries > 0 and user_pass != secret_pass:                                              # ეს ფუნქცია იმოქმედებს მანამ სანამ შეყვანილი პაროლი არ დაემთხვევა უსაფრთხოების პაროლს ან მცდელობების რაოდენობა არ ამოიწურება
#     user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")    # ეს კოდი უშვებს ბრძანებას რომ შეიყვანოს პაროლი მანამ სანამ შეყვანილი პაროლი არ დაემთხვევა უსაფრთხოების პაროლს ან მცდელობების რაოდენობა არ ამოიწურება
#     tries = tries - 1                                                                      # მცდელობების რაოდენობა კლებულობს 1 ით მანამ სანამ შეყვანილი პაროლი არ დაემთხვევა უსაფრთხოების პაროლს ან მცდელობების რაოდენობა არ ამოიწურება

# if user_pass == secret_pass:                                                               # თუ მომხმარებლის შეყვანილი კოდი დაემთხვევა საიდუმლო კოდს --> 
#     print("Access granted!")                                                               # --> მასში არსებული პრინტ ფუნქცია გააქტიურდება და დაბჭდავს "Access granted"-ს
# elif tries == 0:                                                                           # თუ მცდელობების რაოდენობა გაუტოლდება ნულს და მომხმარებელი ვერ შეძლებს სწორი პაროლის შეყვანას -->
#     print("You've reached the maximum number of tries. Access denied!")                    # --> მასში არსებული პრინტ ფუნქცია გააქტიურდება და დაბჭდავს "You've reached the maximum number of tries. Access denied!"-ს
# else:                                                                                      # თუ ზემოთ ნახსენები პირობებიდან არცერთი არ შესრულდება -->
#     print("Access denied! Try again.")                                                     # --> მასში არსებული პრინტ ფუნქცია გააქტიურდება და დაბჭდავს "Access denied! Try again."



# # 2) დაითვალეთ რამდენი ლუწი რიცხვია 1-დან 50-ის ჩათვლით(გამოიყენეთ for loop-ი)

# Amount = 0
# for i in range(1, 50 + 1):    # 50-ის ჩათვლით
#     if (i % 2) == 0:
#         Amount += 1
#     i += 1
# print("There Is " + str(Amount) + " Even Numbers From 1 To 50")



# # 3) დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული.
# # გამოიყენეთ while loop-ი.
# # (დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)

# sum = 0
# Amount = 0
# while Amount < 100:      # 100-მდე , 99-ის ჩათვლით
#     if (Amount % 2) == 0:
#         sum += Amount
#     Amount += 1
# print("The Sum Of Even Numbers Between 1 And 100 Is " + str(sum))



# # 4) დაბეჭდეთ ყველა რიცხვი 1-დან 30-მდე, რომელიც იყოფა 3-ზე(გამოიყენეთ while loop-ი)

# Numbers = 1
# while Numbers < 30:         # 30-მდე , 29-ის ჩათვლით
#     if (Numbers % 3) == 0:
#         print(str(Numbers) + " Can Be Divided By 3 Without Remainders")
#     Numbers += 1



# # 5) მომხარებელს შემოატანინეთ რიცხვი 
# # და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)
 
# Divisible = int(input("Choose Number to search for its Dividers: " ))
# Divider = Divisible

# while Divider > 0:
#     if (Divisible % Divider) == 0:
#         print(str(Divider) + " Is Divider For " + str(Divisible))
#     Divider -= 1



# # 6) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს 
# # და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია

# Number = float(input("Enter The Number: " ))

# if Number < 0:
#     print("Its Negative")
# elif Number == 0:
#     print("Its 0")
# else:
#     print("Its Positive")



# # 7) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს 
# # და გაიგებს არის თუ არა ის ნაკიანი(წელი როდესაც თებერვალში 29 დღე გვაქვს). 
# # ნაკიანი არის წელი თუ ის იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე.(გამოიყენეთ and და or ოპერატორები)

# Year = int(input("Enter The Year: " ))

# if (Year % 400) == 0 and (Year % 100) == 0:                                         # if (Year % 400) == 0:
#     print(str(Year) + " Is The Leap Year")                                          #     print(str(Year) + " Is The Leap Year")
# elif (Year % 4) == 0 and (Year % 100) != 0:                                         # elif (Year % 100) == 0:
#     print(str(Year) + " Is The Leap Year")                                          #     print(str(Year) + " Is Not The Leap Year")
# else:                                                                               # elif (Year % 4) == 0:
#     print(str(Year) + " Is Not The Leap Year")                                      #     print(str(Year) + " Is The Leap Year")                                                                                  # else:
#                                                                                     # else:
#                                                                                     #     print(str(Year) + " Is Not The Leap Year")




# 8) მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). 
# თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", 
# თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B", 
# თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", 
# სხვა შემთხვევაში გამოუტანეთ "Your grade is D"

Score = int(input("Enter The Number Between 1 And 100: " ))
if 0 > Score or Score > 100:
    print("Your selected number does not meet the above criteria")    
elif 90 < Score <= 100:
    print("Your grade is A")
elif 80 < Score <= 90:
    print("Your grade is B")
elif 70 < Score <= 80:
    print("Your grade is C")
else:
    print("Your grade is D")


