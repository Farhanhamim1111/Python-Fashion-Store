import random
import time

#Inventory -----------------------------------------
ShoeInventory = {
  "Nike Jordans Low": 49, 
  "Converse Chuck Taylors": 26, 
  "Adidas Superstars": 34,
  "New Balance 530s": 37,
  "Fashion Fantasy Shoes": 100
}

SweaterInventory = {
  "Nike Tech ": 16,
  "Adidas three stripe": 41,
  "Puma Essential Hoodie": 45,
  "Reebok Classics": 32,
  "Fashion Fantasy Sweaters": 100
}

ShirtInventory = {
  "U.S. Polo Assn": 31,
  "Adidas 3-Striped Tee": 23,
  "Plain white tee": 43,
  "Puma Big Cat": 46,
  "Fashion Fantasy Tees": 100
}

PantsInventory = {
  "Adidas Track Pants": 44,
  "Jeans": 47,
  "Under Armour Shorts": 22,
  "Cargo Pants": 28,
  "Fashion Fantasy Pants": 100
}

HatsInventory = {
  "Nike Cap": 50,
  "White colored cap": 29,
  "Sun hat": 38,
  "British Caps": 10,
  "Fashion Fantasy Hats": 100
}

DressInventory = {
  "Satin dresses": 30,
  "Sundresses": 24,
  "Wedding dresses": 10,
  "Floral dresses": 20
}

SockInventory = {
  "Nike Dri-Fits": 34,
  "Puma Repreve": 44,
  "Adidas Trefoil": 54,
  "Reebok Basic Lowcut": 12,
  "Fashion Fantasy Socks": 100
}

TotalInventory = {
  **ShoeInventory,
  **PantsInventory,
  **ShirtInventory,
  **SweaterInventory,
  **HatsInventory,
  **DressInventory,
  **SockInventory
}

#Prices---------------------------------------------
ShoePrices = {
  "Nike Jordans Low": 74.99, 
  "Converse Chuck Taylor All Stars": 47.99, 
  "Adidas Superstars": 86.99,
  "New Balance 530s": 57.99, 
  "Fashion Fantasy Shoes": 0.01
}

SweaterPrices = {
  "Nike Tech ": 75.99,
  "Adidas three stripe": 23.99,
  "Puma Essentials Hoodie": 25.99,
  "Reebok Classics": 23.99,
  "Fashion Fantsy Sweaters": 0.01
}

ShirtPrices = {
  "U.S. Polo Assn": 14.99,
  "Adidas 3-Striped Tee": 29.99,
  "Plain white tee": 2.99,
  "Puma Big Cat": 14.99,
  "Fashion Fantasy Shirts": 0.01
}

PantsPrices = {
  "Adidas Track Pants": 24.99,
  "Jeans": 9.99,
  "Under Armour Shorts": 19.99,
  "Cargo Pants": 4.99,
  "Fashion Fantasy Pants": 0.01
}

HatsPrices = {
  "Nike Cap": 19.99,
  "White colored cap": 4.99,
  "Sun hat": 16.99,
  "British Caps": 4.99,
  "Fashion Fantasy Hats": 0.01
}

DressPrices = {
  "Satin dresses": 34.99,
  "Sundresses": 23.99,
  "Wedding dresses": 69.99,
  "Floral dresses": 18.99
}

SockPrices = {
  "Nike Dri-Fits": 24.99,
  "Puma Repreve": 21.99,
  "Adidas Trefoil": 13.99,
  "Reebok Basic Lowcut": 11.99,
  "Fashion Fantasy Socks": 0.01
}

TotalPrices = {
  **ShoePrices,
  **PantsPrices,
  **ShirtPrices,
  **SweaterPrices,
  **HatsPrices,
  **DressPrices,
  **SockPrices
}

#Seperation ----------------------------------------
def Buy(item, quantity):
  print(f"You have ordered {quantity} {item}.")

#These functions are to check how much each item is
def ShoePrice():
  for item, quantity in ShoePrices.items():
   print(f"\n{item}: {quantity}")

def SweaterPrice():
  for item, quantity in SweaterPrices.items():
   print(f"\n{item}: {quantity}")

def ShirtPrice():
  for item, quantity in ShirtPrices.items():
   print(f"\n{item}: {quantity}")

def PantPrice():
  for item, quantity in PantsPrices.items():
   print(f"\n{item}: {quantity}")

def HatPrice():
  for item, quantity in HatsPrices.items():
   print(f"\n{item}: {quantity}")

def DressPrice():
  for item, quantity in DressPrices.items():
   print(f"\n{item}: {quantity}")

def SockPrice():
  for item, quantity in SockPrices.items():
    print(f"\n{item}: {quantity}")

#These functions are to check how much items are in stock
def checkShoe():
  for item, quantity in ShoeInventory.items():
   print(f"\n{item}: {quantity}")

def checkSweater():
  for item, quantity in SweaterInventory.items():
   print(f"\n{item}: {quantity}")

def checkShirt():
  for item, quantity in ShirtInventory.items():
   print(f"\n{item}: {quantity}")

def checkPants():
  for item, quantity in PantsInventory.items():
   print(f"\n{item}: {quantity}")

def checkHats():
  for item, quantity in HatsInventory.items():
   print(f"\n{item}: {quantity}")

def checkDress():
  for item, quantity in DressInventory.items():
   print(f"\n{item}: {quantity}")
    
def checkSock():
  for item, quantity in SockInventory.items():
    print(f"\n{item}: {quantity}")
    
while True:
  print("\nWelcome to Fashion Fantasy! \nWe have a multitude of attractive "
    "attire to meet your needs and desires. Now, you can either: ")

  print("1. Buy something")
  print("2. Get employed")
  print("3. Check our stock")
  print("4. Check our prices")
  print("5. Check Latest Sale")
  print("6. Leave")

  choice = input("What will you do today? \n")

  if choice == '1':
    print("Make sure to look at our stock before purchasing.")
    print("Do you want to continue, or go back and check our stock?")
    o = input("(<continue> or <check>)\n")
    p = str.lower(o)
    if p == 'continue':
      print("What do you want to buy?")
      item = input("(Shoes, shirts, pants, sweaters, hats, dresses, socks) \n")
      item = str.lower(item)
      if item == 'shoes':
        print(" 1. Nike Jordans Low,\n 2. Converse Chuck Taylors,\n 3. Adidas Superstars,\n 4. New Balance 530s,\n 5. Fashion Fantasy Shoes\n")
        jg = input("Do you want choice 1, 2, 3, 4 or 5?\n")
        if jg == "1":
              print("Okay, you have chosen Nike Jordans Low.\n")
        elif jg == "2":
              print("Okay, you have chosen Converse Chuck Taylors.\n")
        elif jg == '3':
              print('Okay, you have chosen Adidas Superstars.\n')
        elif jg == '4':
              print("Okay, you have chosen New Balance 530s.\n")
        elif jg == '5':
              print("Okay, you have chosen Fahion Fantsy Shoes.\n")
        else:
              print("Please choose an option!")
              break
      elif item == 'sweaters':
          print(" 1. Nike Tech,\n 2. Adidas Three Stripes,\n 3. Puma Essential Hoodie,\n 4. Reebok Classics,\n 5. Fashion Fantasy Sweaters\n")
          jg = input("Do you want choice 1, 2, 3, 4 or 5?\n")
          if jg == "1":
              print("Okay, you have chosen Nike Tech.")
          elif jg == "2":
              print("Okay, you have chosen Adidas Three Stripes.")
          elif jg == '3':
              print('Okay, you have chosen Puma Essential Hoodie.')
          elif jg == '4':
              print("Okay, you have chosen Reebok Classics.")
          elif jg == '5':
              print("Okay, you have chosen Fahion Fantsy Sweaters.")
          else:
              print("Please choose an option!")
              break
      elif item == 'shirts':
        print(" 1. U.S. Polo Assn,\n 2. Adidas 3-Stripe Tee,\n 3. Plain White Tee,\n 4. Puma Big Cat,\n 5. Fashion Fantasy Shirts\n")
        jg = input("Do you want choice 1, 2, 3, 4 or 5?\n")
        if jg == "1":
            print("Okay, you have chosen U.S. Polo Assn.")
        elif jg == "2":
            print("Okay, you have chosen Adidas 3-Stripe Tee.")
        elif jg == '3':
            print('Okay, you have chosen Plain White Tee.')
        elif jg == '4':
            print("Okay, you have chosen Puma Big Cat.")
        elif jg == '5':
            print("Okay, you have chosen Fahion Fantsy Shirts.")
        else:
            print("Please choose an option!")
            break
      elif item == 'pants':
        print(" 1. Adidas Track Pants,\n 2. Jeans,\n 3. Under Armour Shorts,\n 4. Cargo Pants,\n 5. Fashion Fantasy Pants\n")
        jg = input("Do you want choice 1, 2, 3, 4 or 5?\n")
        if jg == "1":
            print("Okay, you have chosen Adidas Track Pants.")
        elif jg == "2":
            print("Okay, you have chosen Adidas Jeans.")
        elif jg == '3':
            print('Okay, you have chosen Under Armour Shorts.')
        elif jg == '4':
            print("Okay, you have chosen Cargo Pants.")
        elif jg == '5':
            print("Okay, you have chosen Fahion Fantsy Pants.")
        else:
            print("Please choose an option!")
            break
      elif item == 'hats':
        print(" 1. Nike Cap,\n 2. White colored cap,\n 3. Sun hat,\n 4. British Caps,\n 5. Fashion Fantasy Hats\n")
        jg = input("Do you want choice 1, 2, 3, 4 or 5?\n")
        if jg == "1":
            print("Okay, you have Nike Cap.")
        elif jg == "2":
            print("Okay, you have chosen White colored cap.")
        elif jg == '3':
            print('Okay, you have chosen Sun hat.')
        elif jg == '4':
            print("Okay, you have chosen British Cap.")
        elif jg == '5':
            print("Okay, you have chosen Fahion Fantsy Hats.")
        else:
            print("Please choose an option!")
            break
      elif item == 'dresses':
        print(" 1. Satin dresses,\n 2. Sundresses,\n 3. Wedding dresses,\n 4. Floral dresses,\n")
        jg = input("Do you want choice 1, 2, 3, 4 or 5?\n")
        if jg == "1":
            print("Okay, you have Satin dresses.")
        elif jg == "2":
            print("Okay, you have chosen Sundresses.")
        elif jg == '3':
            print('Okay, you have chosen Wedding dresses.')
        elif jg == '4':
            print("Okay, you have chosen Floral dresses.")
        else:
            print("Please choose an option!")
            break
      elif item == 'socks':
        print(" 1. Nike Dri-Fits,\n 2. Puma Repreve,\n 3. Adidas Trefoil,\n 4. Reebok Basic Lowcut,\n 5. Fashion Fantasy Socks\n")
        jg = input("Do you want choice 1, 2, 3, 4 or 5?\n")
        if jg == "1":
            print("Okay, you have chosen Nike Dri-Fits.")
        elif jg == "2":
            print("Okay, you have chosen Puma Repreve.")
        elif jg == '3':
            print('Okay, you have chosen Adidas Trefoil.')
        elif jg == '4':
            print("Okay, you have chosen Reebok Basic Lowcut.")
        elif jg == '5':
            print("Okay, you have chosen Fahion Fantsy Socks.")
        else:
            print("Please choose an option!")
            break
      else:
        print("Please choose something!")
        break
      print("You cannot purchase more than a quantity of 50.")
      try:  
        quantity = int(input("How much of that do you want to buy? \n"))
        limit = 50  
        if quantity > limit:
          print("Sorry, but you cannot have an order quantity of more than 50. Your"
              " order has been cancelled. Please try to order again")
          break
        elif quantity < limit:
          print("Okay, give us some time to fetch your order!")
        time.sleep(5)
        Buy(item, quantity)
      except ValueError:
        print("You have to put a number under 50. Your order has been cancelled. Please try again.")
    elif p == 'check':
      print("Okay! Go back and make sure to carefully check our stock.")
    else:
      print("Thats not a proper function. Try to make an order again.")
  elif choice == '2':
    print("Sorry! We're not hiring right now.")
  elif choice == '3':
    print("Do you want to check our stock of: ")
    i = input("Shoes, shirts, sweaters, pants, hats, socks, or dresses? \n")
    j = i.lower()
    if j == 'shoes':
      checkShoe()
    elif j == 'sweaters':
      checkSweater()
    elif j == 'shirts':
      checkShirt()
    elif j == 'pants':
      checkPants()
    elif j == 'hats':
      checkHats()
    elif j == 'dresses':
      checkDress()
    elif j == 'socks':
      checkSock()
    else:
      print("Please choose a clothing category.")
  elif choice == '4':
    print("Do you want to check our stock of: ")
    g = input("Shoes, shirts, sweaters, pants, hats, or dresses? \n")
    h = g.lower()
    if h == 'shoes':
      ShoePrice()
    elif h == 'sweaters':
      SweaterPrice()
    elif h == 'shirts':
      ShirtPrice()
    elif h == 'pants':
      PantPrice()
    elif h == 'hats':
      HatPrice()
    elif h == 'dresses':
      DressPrice()
    elif h == 'socks':
      SockPrice()
    else:
      print("Please choose a clothing category.")
  elif choice == '5':
    percentage = random.randint(1,85)
    percent = str(percentage)
    product, price = random.choice(list(TotalPrices.items()))
    money = str(price)
    print(product + ", " + percent + "% off.")
    print("Price now is:")
    rounded = round((price - (price * percentage/100)), 2)
    print(rounded)
  elif choice == '6':
    print("Okay, have a good day!")
    break
  else:
    print("That is not a proper action!")