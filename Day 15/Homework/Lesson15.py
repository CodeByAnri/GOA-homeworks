# ჩატ-ბოტი არის პროგრამა, რომელიც არის შექმნილი ადამიანთან ურთიერთობისთვის.
# ის იყენებს ხელოვნურ ინტელექტს, რომ გაიგოს შეკითხვა და უპასუხოს მას.
# ჩატ ბოტემს შეუძლიათ შეკითხვებზე პასუხის გაცემა, პერსონალური რეკომენდაცია(თქვენი შეხედულების მიხედვით შემოგთავაზებენ სხვადასხვა პროდუქტებს და ა.შ)...


# 1) თქვენი დავალებაა შექმნათ მარტივი ჩატ-ბოტი, რომელიც კოდის გაშვებისთანავე მიესალმება მომხარებელს და ჰკითხავს "How are your?",
# თუ მომხარებელი შეიყვანს, "Normal" დაბეჭდეთ "Bot:I hope you will get better", სხვა შემთხვევაში თუ შემოიყვანს "Great", დაუბეჭდეთ "Bot:Good! Have a nice day",
# ხოლო თუ შემოიყვანა "Sad" ან "Super Sad" დაუბეჭდეთ "Bot:It's sad".
# საბოლოოდ დაბეჭდეთ "Good bye!" და გათიშეთ while ციკლი.
# ამისათვის მას გადაეცით სწორი პირობა(მინიშნება: შექმენით ცვლადი რომლის მნიშვნელობა თავიდან იქნება False, while ციკლს პირობად გაუწერეთ ეს ცვლადი,
# თუ მომხარებელმა სწორი ინფორმაცია შემოიყვანა მისი ნიშვნელობა გახდება True და როცა ყველა პირობა შესრულდება while ციკლი გაითიშება).
# თუ მომხარებელი შემოიყვანს ისეთ ინფორმაციას რაზეც თქვენი ბოტი არ არის დაპროგრამირებული, დაბეჭდეთ "Bot: Sorry, I didn't understand, repeat."
# (ამ შემთხვევაში while ციკლისთვის შექმნილი ცვლადის მნიშვნელობა არ იცვლება და ციკლი არ წყვეტს მუშაობას)
# დაგჭირდებათ: while loop; input; if/else; and or.
# თქვენი სურვილით დაამატეთ სხვა ფუნქციები და გააუმჯობესეთ ჩატ-ბოტი



Finished = False
print("Hello! How are you? " )

while Finished == False:
    User_Answer = input("Type The Answer To The Question ,,Hello! How are you?'' : ")

    if User_Answer == "Normal":
        print("Bot: I hope you will get better.")
        Finished = True

    elif User_Answer == "Great":
        print("Bot: Good! Have a nice day.")
        Finished = True

    elif User_Answer == "Sad" or User_Answer == "Super Sad":
        print("Bot: It's sad.")
        Finished = True

    else:
        print("Bot: Sorry, I didn't understand, repeat.")


print("Good bye!")




# 2) შექმენით პრეზენტაცია, სადაც ისაუბრებთ თუ როგორ მუშაობს CPU, RAM, GPU. კარგი იქნება თუ დახატავთ



# CPU - პროცესორი, რომელიც არის კომპიუტერის მთავარი შემადგენელი ნაწილი. იგი მოთავსებულია დედაპლატაზე და შეუძლია კომპიუტერი ამუშავოს მხოლოდ კვების ბლოკითა და დედაპლატით.

# ეს მოწმობს ჩემ ზემოხსენებულ განცხადებას. CPU შეუძლია შესრულოს ადამიანების მიერ მიცემული ინსტრუქციები, კოდები, არითმეტიკული და ლოგიკური ოპერაციები.

# მისი სიჩქარე დროთა განმავლობაში იცვლებოდა, და მისი მუშაობის მეთოდიც საგრძნობლად შეიცვალა. პროცესორის სიჩქარე იზომება გიგაჰერცით, რაც ხშირად პროცესორის პერფორმანსის მთავარი კომპონენტია.

# დღესდღეობით, პროცესორები მრავალ ბირთვიან არქიტექტურას იყენებენ, რაც იმას ნიშნავს, რომ ისინი რამდენიმე პროცესორული ბირთვის კომბინაციას შეიცავენ. 
# თითოეული ბირთვი დამოუკიდებლად აწარმოებს ინსტრუქციებს, რაც მნიშვნელოვნად ზრდის კომპიუტერის შესაძლებლობებს, განსაკუთრებით მრავალპროცესორული ოპერაციების დროს. 
# უფრო მეტი ბირთვი საშუალებას აძლევს CPU-ს უფრო ეფექტურად მართოს პარალელური სამუშაოები, რაც აჩქარებს პროცესების შესრულებას და აუმჯობესებს ზოგად ეფექტურობას.






# GPU - გრაფიკული პროცესორი, რომელიც სპეციალიზებულია გამოსახულების და ვიდეოს დამუშავებაში. იგი მუშაობს CPU-სთან ერთად, მაგრამ კონცენტრირებულია პარალელურ პროცესებზე, 
# რაც მას იდეალურად აქცევს გრაფიკული ინფორმაციის, როგორიცაა თამაშები და კომპიუტერული გრაფიკა, სწრაფად და ეფექტურად დამუშავებისთვის.

# GPU-ები აჩქარებენ გრაფიკის-rendering პროცესს და ასევე გამოიყენება დომენებში, როგორიცაა ვირტუალური რეალობა, 
# ხელოვნური ინტელექტი და მონაცემთა ანალიზი. ისინი ახერხებენ დიდი რაოდენობით მონაცემების პარალელურად დამუშავებას, რაც სიჩქარისა და პერფორმანსის ზრდას იწვევს.

# Integrated GPU - ჩაშენებულია CPU-ში და იყენებს კომპიუტერის მეხსიერებას. იდეალურია ყოველდღიური ამოცანებისთვის, მაგრამ მისი გრაფიკული ძალა შეზღუდულია, რაც პრობლემატურია მძიმე თამაშების დროს.

# Dedicated GPU - ცალკე მოწყობილობა, რომელიც უზრუნველყოფს მაღალ გრაფიკულ შესრულებას. იდეალურია რთული თამაშების და პროფესიონალური გრაფიკის სამუშაოებისთვის, თუმცა უფრო ძვირია და მეტი ენერგიის მოხმარებას მოითხოვს.






# RAM (Random Access Memory) - კომპიუტერის დროებითი მეხსიერება, რომელიც ინახავს მონაცემებს და პროგრამებს, რომლებსაც CPU ამჟამად იყენებს. 
# RAM საშუალებას აძლევს პროცესორს ჰქონდეს სწრაფი წვდომა საჭირო ინფორმაციაზე, რაც მნიშვნელოვნად აჩქარებს სისტემის მუშაობას.

# RAM-ის რაოდენობა გავლენას ახდენს კომპიუტერის multitasking შესაძლებლობებზე; მეტი RAM საშუალებას იძლევა რამდენიმე პროგრამის ერთად გაშვების და უკეთესი მულტიმედიური გამოცდილების შექმნის შესაძლებლობას. 
# მას აქვს მაღალი სიჩქარე, მაგრამ ის დროებითია: კომპიუტერის გამორთვისას მისი მონაცემები იშლება.




