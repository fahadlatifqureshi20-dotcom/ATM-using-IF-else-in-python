balance = 5000 
ammount = 0
attempts=0
card = input("Please insert your card: ")
if card == "valid_card":
    while attempts < 3: 
      pin = input("Please enter your PIN: ")
      if pin == "1234":
        break
      else:
        attempts += 1
        print(f"Invalid PIN. {3 - attempts} attempts left.")
        if attempts == 3:
            print("Too many incorrect attempts. Access denied.")
            exit()
    
    print("Access granted. Welcome!")
        
     
                
    while True:    
               
        print("choose option => ","balance check ","withdraw cash ", "exit ") 
    
        option = input()
       

        if option == "exit":
            print("Thank you for using our ATM. Goodbye!")
            exit()

        elif option == "balance check":
          print(f"Your current balance is = ${balance}.")
          

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
             
        else:  print("invalid option! please choose a valid option")   
        print('press 1 to continue or 0 to exit')    
        choice = input()
        if choice == "0":
            print("Thank you for using our ATM. Goodbye!")
            exit()
else:       
    print("Invalid card. Access denied.")
