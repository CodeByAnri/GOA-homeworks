# 1) მომხმარებელს შემოატანინეთ:
# სახელი,
# გვარი,
# ასაკი,
# საცხოვრებელი ადგილი 
# და მეილი.
# კომენტარებით ახსენით რას ნიშნავს თითო ხაზი ამ კოდის


Name = input("Enter Your Name: " )                               # მიუთითე შენი სახელი
Last_Name = input("Enter Your Last Name: " )                     # შენი გვარი
Age = int(input("Enter Your Age: " ))                            # ავკრძალე სტრინგი ამ ინტეჯერ ბრძანებით / შეიყვანე შენი ასაკი
Place_Of_Residence = input("Enter Your Place Of Residence: " )   # საცხოვრებელი ადგილი
Gmail = input("Enter Your Gmail: " )                             # მეილი

print("^^^^^^^^^^^")

print("Individual Named " + Name + " " + Last_Name)              # ოპერატორი დაინახავს შენს სახელს და გვარს
print("Age is " + str(Age))                                      # ასაკს
print("Lives in " + Place_Of_Residence)                          # საცხოვრებელსა და
print("His Email is " + Gmail)                                   # მეილს

print("^^^^^^^^^^^")

# 2) მომხმარებელს შემოატანინეთ ასაკი და დაუპრინტეთ რამდენი წლის იქნება ის 20 წელიწადში

Age = int(input("Enter Your Age: " ))  
print("^^^^^^^^^^^")
Age_After_20_Years = Age + 20
print("In 20 Years You Will Be " + str(Age_After_20_Years))







