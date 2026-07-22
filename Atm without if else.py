balance = 5000 
amount = 0
opt = 0

def card_check():
  '''
  checks if the card is valid or not
  '''
  
  card = input("Please insert your card: ")
  if card == "valid_card":
   return  True
  
  else :
    exit("Invalid card. Please try again.")



def pin_check ():
    '''
     checks if the pin is valid or not
     '''
    attempts=0
    while attempts < 3:
      pin= input("Please enter your PIN: ")
      if pin == "1234":
        print("Access granted. Welcome!")
      
        return True
        
      else:
        attempts += 1
        print(f"Invalid PIN. {3 - attempts} attempts left.")
        if attempts == 3:
            print("Too many incorrect attempts. Access denied.")
            exit()
            
def menu():
    print("Please select an option:")
    print("1. Balance check")
    print("2. Withdraw cash")
    print("3. Exit")
    opt = input()
    return opt
                

def exit_menu ():
  print("Thank you for using our ATM. Goodbye!")
  exit()
     

def balance_check(show_balance):
  
      print(f"Your current balance is = ${show_balance}.")
          
def withdraw(local_balance):
        # if opt == "withdraw cash":
           
          while True:
           print("enter the amount you want to withdraw => .")
         
           amount = int(input())
           if amount<1000 or amount>local_balance or amount%500 != 0:
            print(" dicliend! invalid ammount . press 1 to re-enter the ammount or 0 to exit")
            con=input()
            if con == "1":
              continue
            else:
              exit()  
           else:
            print(f"transection completed! please collect your cash= $ {amount}")
            local_balance -= amount
            print(f"Your remining balance is ${local_balance}. press 1 to continue or 0 to exit")
            if input() == "1":
              continue
            else:   
              return local_balance


if card_check():
  pin_check()  
  
  
actions={"balance check":lambda :balance_check(balance),
    "withdraw cash":lambda :withdraw(balance),
    "exit":exit_menu
    }


    
while True:
  
     choice= menu()  
    
     actions[choice]() 