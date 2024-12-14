a = input("Enter a string")
b = ("")
for i in a:
    b = i + b
    
print("original string",a)
print("reversed string",b)