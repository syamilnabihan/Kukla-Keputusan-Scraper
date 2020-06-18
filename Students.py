class student():
    def __init__(self, name, nk, ic, tpng):
        self.name = name
        self.matrixnum = nk
        self.icnum = ic
        self.tpng = tpng

    def cgpa(self):
        print(self.name,"tpng is",self.tpng)

person = student("Hal", "djjd", "ddff",3.44 )
print(person.tpng)