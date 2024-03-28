import re
import string
a = "^[a-z A-Z]+$"
b = "^[0-9]+$"
c = "^[a-z A-Z]+[@]+[0-9]+$"   
  
x = input() or "none"
y = input() or "none"
z = input() or "none"
class fun:
    def __init__(self, x ,y,z):
        if(re.search(a,x)):
            self.x = x
            if(re.search(b,y)):
                self.y = y
                self.z = z
            else:
                self.y = z
                self.z = y

        elif(re.search(b,x)):
            self.y = x
            if(re.search(a,y)):
                self.x = y
                self.z = z
            else:
                self.x= z
                self.z = y
        else:
            self.x = z
            if(re.search(b,y)):
                self.y = y
                self.z = x
            else:
                self.y = x
                self.z = y
        
    def printstuff(self):
        print("*******************************************************************************")
        print(f'Name:  {self.x}')
        print(f'roll:  {self.y}')
        print(f'ID :   {self.z}')
m = fun(x,y,z)
m.printstuff()

        
 
