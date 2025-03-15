class Library:
    def __init__(self):
        self.books=[]
        self.nobooks=0
    def addbook(self,name):
        self.books.append(name)
        self.nobooks+=1
    def showbooks(self):
        for i in self.books:
            print(i)

a=Library()
a.addbook("Hi")
a.addbook("biii")
a.addbook("helloo")
a.showbooks()
print(a.books)
print(a.nobooks)
print("******************")
b=Library()
b.addbook("Hi")
b.addbook("biii")
b.addbook("helloo")
b.showbooks()
print(b.books)
print(b.nobooks)