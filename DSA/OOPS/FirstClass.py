class Atm:
    def __init__(self) -> None:
        print("First Class \n")
        
        self.pin=0
        self.balance=0
        self.menu()
        pass

    def menu(self):
        user_input=input(""" 
                            Hello How Would you Proceseed?
                            1. Enter 1 to Create the pin\n
                            2. Enter 2 to Change pin\n
                            3. Enter 3 to Deposit Money\n
                            4. Enter 4 to Withdraw\n
                            5. Enter 5 to Check Balance \n""")
        if  user_input=='1':
            self.Create_pin()
        elif user_input=='2':
            self.Change_pin()

        if  user_input=='3':
            self.Deposit_Amount()
                
        elif user_input=='4':
            self.WithDrawAmount()  

        elif user_input=='5':
            self.checkbalance()   
        elif user_input=='6':
            self.exit()
            print("Bye")  

    def Create_pin(self):
        self.pin=(int)(input("Enter the pin \n"))
        
        print("Pin Set")

        user_balance=(int)(input("Enter the Balance for your First Time \n"))
        self.balance=user_balance
        print("This {} Amount Deposit Succussfully",user_balance)
        self.menu()

    def Change_pin(self):
        temp=(int)(input("Enter the pin \n"))
        if temp==self.pin:
            self.pin=(int)(input("Enter new pin \n"))
            print("Pinned Changed")
            pass
        else :
            print("Invaild Pin")

        self.menu()

    def Deposit_Amount(self):
        temp=(int)(input("Enter the pin \n"))
        if temp==self.pin:
            addamount=(int)(input("Enter the Amount"))
            self.balance=self.balance+addamount
            print("This much amount is Add",addamount)
        else :
            print("Invalid Pin")  
            print("Try Again!!!!") 
        self.menu()

    def WithDrawAmount(self):
        temp=(int)(input("Enter the pin \n"))
        if temp==self.pin:
            withDraw=(int)(input("Enter the Amount to Withdraw"))
            self.balance=self.balance-withDraw
            print("This much amount is deduct",withDraw)
        else :
            print("Invalid Pin")    
        self.menu()    
    
    def checkbalance(self):
        temp=(int)(input("Enter the pin \n"))
        if temp==self.pin :
            print("Available Balanace",self.balance)
        else  :
            print("Invalid Pin")
        self.menu()    
   
    def exit(self):
        print('Thank For Using have a Good Day')

