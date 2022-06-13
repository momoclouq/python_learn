class myclass:
    name = "blah";

    def __init__(self, name) -> None:
        self.name = name;

    def func1(self):
        print("this is a message inside the class");

val1 = myclass('minh');
print(val1.name);

#dictionary
phonebook = {}
phonebook["John"] = 11111;
phonebook["Tim"] = 22222;
phonebook['James'] = 33333;

print(phonebook);

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook["John"];

print(phonebook);

def call_me():
    print("call me");