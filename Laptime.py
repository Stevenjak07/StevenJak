class constructorExample:
# constructor
    def __init__(self, name):
        self.name = name
        self.genders = "Female"
        print('Constuctor Called ')
# A Method in the class
    def welcomeText(self):
        print('Welcome to theasdgsagsadg ' + self.name + ' club')
obj = constructorExample('Linna pocket okay bong jack nh dg hx sak lerk ti 2')
print(obj.name)
obj.welcomeText()