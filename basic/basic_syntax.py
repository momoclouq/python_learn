# #printing
# print("Hello world");

# #variables and types
# #completely object oriented, not 'statically typed'
# #every variable is an object
# myint = 7;
# print(myint);

# myfloat = 7.3;
# print(myfloat);

# myfloat2 = float(7);
# print(myfloat2);

# #strings
# mystring = 'Hello'
# mystring2 = "Hello"
# mystring3 = "Hello 'welcome'"
# print(mystring + '-' + mystring2, mystring3);

# a, b=1, 2;
# print(a, b);

# print(mystring + str(b) + str(myfloat2));

# #list
# mylist = [];
# mylist.append(1);
# mylist.append(2);
# mylist.append(3);
# mylist.append('something else');

# print(mylist[0]);
# print(mylist[1]);
# print(mylist[2]);
# print(mylist[3]);

# for x in mylist:
#     print("loop: " + str(x));

#list exercises
numbers = [];
strings = [];
names = ['minh', 'loco', 'lbolo'];

for i in range(3):
    numbers.append(i + 1);

for number in numbers:
    strings.append(str(number) + " value");

print(numbers);
print(strings);

# operators
value = 1 + 3 + 5;
print(value);

value2 = 3 ** 4;
print(value2);

lotsofhellos = "hello" * 10;
print(lotsofhellos);

#concatenate list
even_numbers = [2,4,6,8];
odd_numbers = [1,3,5,7];
all_numbers = odd_numbers + even_numbers;
print(all_numbers);