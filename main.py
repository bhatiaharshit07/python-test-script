import os

file1 = open("pid.txt", "w")
file1.write(str(os.getpid()))
file1.close() 

print(os.getpid())
print("HIIII")
print("Hellooooo")

a = 5
b = 6

while True:
    print("hello this is true")
