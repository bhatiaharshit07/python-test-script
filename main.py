import os

file1 = open("pid.txt", "w")
file1.write(str(os.getpid()))
file1.close() 

print(os.getpid())
print("HIIII")

a = 5
b = 6

while True:
    print("hello")
