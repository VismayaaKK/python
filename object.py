#object oriented
class college:
    def students(self,name):
        self.name=name
        print(self.name)

st1=college()
st1.students("aa")
st2=college()
st2.students("bbb")

if(id(st1)==id(st2)):
    print("true")
else:
    print("false")

#procedural
a=9
b=9
if(id(a)==id(b)):
    print("true")
else:
    pass

class child:

    def __init(self)->None:
        print("class child")
    
    def printname(self,new):
        self.new=new
        print(self.new)

s=child()
s.printname("ff")

#checking whether it is working or not.
class addition():
    def __init__(self)-> None:
        print("class is working. . .")

#loading variables
    def var(self,a,b):
        self.a=a
        self.b=b
#perform addition
    def add(self):
        self.c=self.a+self.b
#printing result

    def printresult(self):
        print(self.c)

        #creating object
f=addition()
f.var(3,5)
f.add()
f.printresult()

#qn2:creating class with names:
class names():
    def __init__(self) -> None:
        print("working")

    def var(self,frame,lname):
        self.fname=fname
        self.lname=lname
    def add(self):
        self.name=self.fname+self.lname
    def printresult(self):
        print(self.name)
    d=names()
    d.var("rr","aaa")
    d.add()
    d.printresult()


#qn3:
class Classes():
    def __init__(self) -> None:
        print("class Classes")
    def studentdetails(self):
        self.name=input("enter the name")
        self.id=input("enter the id")
        self.place=input("enter the place")
        self.age=input("enter the age")
    def printinfo(self):
        print("##"*30)
        print("name is : "+self.name+"\nid is"+self.id+"\nplace is "+self.place+"\nage is "+self.age)
    p=Classes()
    p.studentdetails()
    p.printinfo()
    class sub(Classes):
        def __init__(self) -> None:
            print("class sub....")

    b=sub()
    b.studentdetails()
    b.printinfo()
