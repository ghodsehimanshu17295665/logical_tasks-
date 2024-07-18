# string method:-
a = "Hello, World!"
print(a.upper())  # upper() Method :- HELLO, WORLD!
print(a.lower())  # LOWER() Method :- hello, world!


b = "    Hello, World!   "
print(b.strip())  # removes any whitespace from the beginning or the end

print(a.replace("H", "J"))  # Replace String:- Jello, World


z = "Together Everyone Achives More"  # split method()
print(z.split())  # ['Together', 'Everyone', 'Achives', 'More']

print(
    z.index("Everyone")
)  # index() method:-ndex() method finds the first occurrence of the specified value.
print(z.index("e"))
# print(z.index("Ram")) #ValueError: substring not found

print(z.find("Everyone"))  # find() method
print(z.find("e"))
print(z.find("Ram"))  # returns -1 if the value is not found.


txt = "hello, and welcome to my world."
print(txt.capitalize())  # capitalize method

txt2 = "Hello, And Welcome To My World!"
print(txt2.casefold())  # casefold method

# join method:-
txt3 = ["Together", "Everyone", "Achives", "More"]
x = " ".join(txt3)
print(x)
