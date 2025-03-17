class constructorExample:
# constructor
    def __init__(self, name):
        self.name = name
        self.genders = "Female"
        print('Constuctor Called ')
# A Method in the class
    def welcomeText(self):
        print('Welcome to the ' + self.name + ' club')
obj = constructorExample('Linna xnxx')
print(obj.name)
obj.welcomeText()