

class sorting:
    def __init__(self):
        self.list1=[]
    def input(self):
        for i in range(1,10):
            a=int(input("Enter the number "))
            self.list1.append(a)
    def output(self):
        a=int(input("Enter the number you want to see in array "))
        i=0
        while i<len(self.list1):
            if(self.list1[i]==a):
                print("Value found at index ... ",i)
                break
            i+=1
        else:
            print("Value not found ! ")
s1=sorting()
s1.input()
s1.output()



