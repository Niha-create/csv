


class student:
    college="fiit"
    def __init__(self,college):
        print("contructor called")
        self.college=college
        
    def greet(self):
        print("welcome")

obj =student("viit")
# obj.college="viit"
print(obj.college)

obj1 =student("dkm")
# obj1.college="dkm"
print(obj1.college)

obj.greet()

