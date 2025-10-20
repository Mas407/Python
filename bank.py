

class bank:
    
    def __init__(self):
        print("Welcome to  Bank")
        print("1. Withdral\nDeposit")
        a=int(input("How i can help you guys"))
        if(a==1):
            self.withdrawal()
        if(a==2):
            self.deposit()     

    
    @staticmethod
    def deposit():
        a=int(input("Enter the amount you want to deposit"))
        f=open("exchange.txt","r")
        data=int(f.read())
        print("Perivious balance ",data)
        t=data+a
        print(t)
        print("Total balance now ",t)
        f.close()
        d=open("exchange.txt","w")
        balance=d.write(str((t)))
        d.close()
    
    @staticmethod        
    def withdrawal():
        a=int(input("Enter the amount you want to withdrwal"))
        
        f=open("exchange.txt","r")
        data=int(f.read())
        if(a<=data and data>=a):
             print("Withdrwal successfull  "," ",a)
        else:
          pass   
        f.close()
        new_balance=data-a
        m=open("exchange.txt","w")
        data1=m.write(str(new_balance))
        m.close()
        print("Total balance is ",new_balance)
s1=bank()


