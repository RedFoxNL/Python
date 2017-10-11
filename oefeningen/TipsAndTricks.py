#Het achterstevoren zetten van een zin
class string_to_word():
    def __init__(self, string):
        self.string = string
        newString = self.string.split(' ')
        newString = newString[::-1]
        print(newString)

#get_and_print_string klasse om zinnen om te zetten naar hoofdletters
class get_and_print_string_upper():
    def __init__(self):
        string = input("What is the sentence?: ")
        print(string.upper())

#get_and_print_string klasse om zinnen om te zetten naar kleine letters
class get_and_print_string_lower():
    def __init__(self):
        string = input("What is the sentence?: ")
        print(string.lower())


#Write a Python class named Rectangle constructed by a length and width and a method
#which will compute the area of a rectangle.
class rectangle():
    def __init__(self, length, width):
        self.length= length
        self.width = width
        anwser = (self.length * self.width)
        print(anwser)



rectangle(5,4)
string_to_word("hello .py")
get_and_print_string_upper()
get_and_print_string_lower()