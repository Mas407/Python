
class check:
    def __init__(self):
        self.list1=[]
    def input(self):
        for i in range(1,10):
            a=int(input("Enter the value you want to store in list "))
            self.list1.append(a)
    def output(self):
        s=0
        e=len(self.list1)-1
        los=-1
        while s<=e:
            mid=s+e//2
            if(self.list1[mid]==n):
                print("Value found at index ",mid)
                loc=mid
                break
            elif(self.list1[mid]<n):
                s=mid+1
            else:
                e=mid-1
        if(loc!=-1):
            pass
        else:
            print("value not found ")
    def update(self):
        b=int(input("Enter the index "))
        a=int(input("Enter the new value  "))
        self.list1.insert(b,a)
        print(self.list1)
    def deletev(self):
        b=int(input("Enter the index "))
        # a=int(input("Enter the new value  "))
        self.list1.pop(b)
        print(self.list1)
s1=check()
s1.input()
n=int(input("Enter the value you want to check in list "))
s1.output()
s1.update()
s1.deletev()

# agr ham cha raha han idex da or jo index ma value ha delete ho jya to --> pop(index)
# agr value batanie ha specific to ham --> remove(value)
# agr ham na delete karna ha index he woha sa to   del.list[1]
# agr zayda index delete karna ho means jo value ha unsa delete ho jaya to 
#               -->    del.list[1:3] 


