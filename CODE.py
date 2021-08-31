Fruits = ("apple" , "banana" , "coconut" , "orange" ,  "pineapple" , "papaya" ,  "mango" , "guava" , "lemon" , "watermelon" , "wood apple" , "apricots" , "almond" , "avocado" , "barberry" , "black currant" , "blackberry" , "blueberry" , "breadfruit" , "cashews" , "cherry" , "custard apple" , "date fruit" , "dragon fruit" , "fig fruit" , "gooseberry" , "grapefruit" , "grapes" , "jackfruit" , "kumquat" , "lychee" , "macadamia nut" , "mulberry" , "nut" , "olive fruit" , "peach" , "pear" , "pistachio" , "plum" , "pomegranate" , "pomelo" , "raisins" , "sapota" , "starfruit" , "sweet Lime" , "tamarind" , "water caltrop" , "acai berry" , "muskmelon" , "prickly pear" , 'jujube' , 'strawberry' , 'cashew' 'apple' , 'quince' , 'passion fruit' , 'palm fruit' , 'persimmon' , 'raspberry' , 'red banana' , 'soursop fruit' , 'kiwi' , 'loquat' , 'malta fruit' , 'mimusops' , 'dates' , 'elderberry' , 'monk fruit' ,  'makoy fruit' , 'cloudberry' , 'cranberry' , 'damson' , 'feijoa' , 'goji berry' , 'honeyberry' , 'huckleberry' , 'jabuticaba' , 'kiwano' , 'mangosteen' , 'miracle fruit' , 'nance' , 'pineberry' , 'salak' , 'satsuma' , 'star apple' , 'surinam cherry' , 'tamarillo' , 'ugli fruit' , 'palmyra fruit' , 'kadamba fruit' , 'jicama fruit' , 'grewia asiatica' , 'pithecellobium dulce' , 'monkey fruit' , 'mandarin' , 'limonia acidissima' , 'black nightshade' )

print ('Welcome to the "FRUITS WORLD "')
number = int(input("How many fruits names you wants to enter ?   : "))

user = []
w = 1
while w<=num :
    fruit = input("Enter the fruit name : ")
    if fruit.lower() in Fruits and fruit.lower() not in user :
        user.append(fruit.lower())
    if fruit.lower() not in Fruits :
        print ("The ", fruit , " is either Not a Fruit or you have misspelt it .")
    

    w = w + 1

print ("\nFruits entered by you are : ")

for user_fruit in user :
    print (user_fruit.title())

print ("\nYOUR SCORE : " , len(user),"/" , len(Fruits) , "  (", (len(user)/len(Fruits))*100 , "%)" )
