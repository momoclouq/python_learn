print()
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

# list exercises
# numbers = [];
# strings = [];
# names = ['minh', 'loco', 'lbolo'];

# for i in range(3):
#     numbers.append(i + 1);

# for number in numbers:
#     strings.append(str(number) + " value");

# print(numbers);
# print(strings);

# # operators
# value = 1 + 3 + 5;
# print(value);

# value2 = 3 ** 4;
# print(value2);

# lotsofhellos = "hello" * 10;
# print(lotsofhellos);

# #concatenate list
# even_numbers = [2,4,6,8];
# odd_numbers = [1,3,5,7];
# all_numbers = odd_numbers + even_numbers;
# print(all_numbers);

# string formatting
# name = "James";
# name2 = "Minh";
# num = 12;
# print('name: %s' % (name));
# print('name1: %s, name2: %s' % (name, name2));
# print('name1: %s, name2: %s, num1: %d' % (name, name2, num));
# # basic format:
# # %s string (or any object with a string representation)
# # %d Integers
# # %f float
# # %.4f - float with fixed amount of digits to the right of the dot
# # %x/%X integer in hex representation
# print();

# data = ("John", "Doe", 53.44);
# format_string = "Hello %s %s. Your current balanace is $%.2f.";
# print(format_string % data);

# string operations
# num1 = 1;
# num2 = 3;
# string = "abcdef abcde efghk";
# print(len(string));
# print(string.count('a'));
# print(string.find('b'));
# print(string[num1:num2]);
# print(string.lower());
# print(string.upper())

# #reverse a string
# print(string[::-1]);
# print(string.startswith("abc"));
# print(string.endswith("def"));
# print(string.split(" "));

s = "Hey thera! what shou"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
