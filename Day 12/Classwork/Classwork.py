# 1) მომხარებელს შემოატანინეთ ორი რიცხვი, 
# აიყვანეთ ისინი მე-3 ხარისხში 
# და გაიგეთ მათი ჯამი, 
# თუ ჯამი ლუწია დაპრინტეთ "Result is Even", 
# სხვა შემთვევაში "Result is Odd"
# აღწერეთ თითოეული მოქმედება კომენტარებით

 
Number1 = int(input("Enter The First Number: " ))             # ცვლადის დეკლარიზაცია და ინიციალიზაცია input-ის დახმარებას 
Number2 = int(input("Enter The Second Number: " ))            # რომელიც გვეხმარება მომხმარებლის მიერ მონაცემის შემოტანაში

Number1 = Number1 ** 3                        # აგვყავს Number1 და Number2 კუბში ანუ მესამე ხარისხში
Number2 = Number2 ** 3

Sum = Number1 + Number2                                       # ვიგებთ Number1 და Number2-ის ჯამს

if (Sum % 2) == 0:                                           # if ფუნქციის დახმარებით გამოგვაქ პასუხი კითხვაზე ჯამი ლუწია თუ კენტი
    print("Result is Even")
else:
    print("Result is Odd")







