# 1) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას, 
# ფუნქციამ ამ წინადადების თითოეული სიტყვა უნდა შეინახოს სიაში, როგორც ცალკე ელემენტი. 
# საბოლოოდ გადააქციეთ სია ისევ წინადადებად, სადაც სიტყვებს შორის არის მძიმე და ერთი დაშორება(", ")

def split_join_sentence(sentence):
    word = ""
    word_list = []
    for i in sentence:
        if i == " ":
            word_list.append(word)
            word = ""
        else:
            word += i
    if i != "":
        word_list.append(word)
    sentence = ", ".join(word_list)
    print(sentence)

sentence = input("Enter Sentence Here: " )

split_join_sentence(sentence)



# 2) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)

def word_symbol_count(sentence2):
    sentence2 = sentence2.split()
    symbol_count_list = []
    for word in sentence2:
        symbol_count_list.append(len(word))
    print(symbol_count_list)

sentence2 = input("Enter Sentence Here: " )

word_symbol_count(sentence2)



# 3) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, 
# სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space). 
# თქვენი დავალებაა ჩამოაშოროთ გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს). 
# საბოლოოდ დააბრუნეთ ეს წინადადება

def remove_excess_spaces(sentence3):
    sentence3 = sentence3.split(" ")
    word_list = []

    for word in sentence3:
        if word != "":
            word_list.append(word)
    sentence3 = " ".join(word_list)
    print(sentence3)

sentence3 = input("Enter Sentence Here: " )

remove_excess_spaces(sentence3)



# 4) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, 
# და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). 
# საბოლოოდ კი აბრუნებს მას

def change_of_spaces(sentence4):
    sentence4 = sentence4.split()
    sentence4 = "-".join(sentence4)
    print(sentence4)

sentence4 = input("Enter Sentence Here: " )

change_of_spaces(sentence4)



# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება. 
# თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და დააბრუნოთ(სიტყვების სიმბოლოები არ უნდა იყოს შებრუნებული)

def reversed_sentence(sentence5):
    sentence5 = sentence5.split()
    sentence5 = sentence5[::-1]
    sentence5 = " ". join(sentence5)
    print(sentence5)

sentence5 = input("Enter Sentence Here: " )

reversed_sentence(sentence5)