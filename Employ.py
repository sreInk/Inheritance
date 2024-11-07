class Person(object):
    def __init__(self,name,Idnumber):
        self.name = name
        self.Idnumber = Idnumber
    def display(self):
         print(self.name)
         print(self.Idnumber)

class Employ(Person):
    def __init__(self, name, Idnumber,salery,Post):
                 self.salery = salery
                 self.Post = Post
                 Person.__init__(self,name,Idnumber)

a = Employ("Rahul Pailikar",124875445,-2000,"cleark")
a.display()
       
        