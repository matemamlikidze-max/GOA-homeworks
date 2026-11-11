
num1=int(input("მართკუთხედის ფართობი"))
width=22
height=2.5
print(width*height)
print("მართკუთხედის ფართობი არის 55.0")


#2
number = int(input(50))

if number % 2 == 0:
    print("რიცხვი ლუწია")
else:
   print("რიცხვი კენტია")




#3
age=16

if age >= 18:
    print("მოგესალმებით, თქვენ სრულწლოვანი ხართ!")
else:
    print("შესვლა შეზღუდულია" )


#4
temperature=-1
if temperature <0:
    print("გარეთ ყინავს ჩაიცვი თბილად")
else:
    print("ძალიან ცხელა!")


#5
balance = 500
balance = input("withdraw amount")
print("balance = balance - withdraw amount")
if balance >= 500:
    print("თანხა აღარ დარჩა კარტაზე")
else:
    print("გამოტანილია")



#6

total_price=79

if total_price>=100:
    print("20%-იანი ფასდაკლება")
else:
   print("10%-იანი ფასდაკლება")

#7
correct_password = "python123"

correct_password=input("password")

if correct_password == "python123":
     print("password is corrrect")
else:
     print("password is incorrect")

#8
score=49
if score >91<100:
     print("u got A")

if score >81<90:
     print("u got B")

if score >71<80:
     print("u got C")

if score >61<70:
     print("u got D")

if score >51<70:
   print("u got E")

if score <=51:
     print("ჩაიჭერი")

#9
total_seconds=50000
print(total_seconds//60)
print (total_seconds%3)
if total_seconds >60:
     print("ეს ერთ საათზე მეტია")
else:
     print("ეს ერთ სააათზე ნაკლებია")

#10

item_name = input("კოკაკოლა:")
price = float(input("ნაყინი: "))
quantity = int(input("ფანტა: "))

total_cost = price * quantity

if total_cost > 50:
    has_discount = True
else:
    has_discount = False



