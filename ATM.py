balance = 5000 
ammount = 0
card = input("Please insert your card: ")
if card == "valid_card":
    pin = input("Please enter your PIN: ")
    
    if pin == "1234":
        print("Access granted. Welcome!")

        print("choose option => ","balance check ","withdraw cash ", "exit ") 

        option = input()
       

        if option == "exit":
            print("Thank you for using our ATM. Goodbye!")
            exit()

        elif option == "balance check":
          print(f"Your current balance is ${balance}.")
          exit()

        elif option == "withdraw cash":
         print("enter the amount you want to withdraw => .")

         ammount = int(input())
         if ammount<1000 or ammount>balance or ammount%500 != 0:
            print(" dicliend! invalid ammount")
            exit() 
         else:
            print(f"transection completed! please collect your cash= $ {ammount}")
            balance=balance-ammount
            print(f"Your remining balance is ${balance}.") 
             
        elif option not in ["balance check", "withdraw cash", "exit"]:
            print("invalid option! please choose a valid option")      
    else:
        print("Invalid PIN. Access denied.")
