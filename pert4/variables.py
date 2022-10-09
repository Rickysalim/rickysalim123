# python variables
# x adalah int
x = 5
# y adalah string
y = "John"
print(x)
print(y)

# multiple values
x, y, z = "ani", "budi", "toni"
print(x)
print(y)
print(z)

print (x,y,z)

# Global Variables
a = "budi"

def func():
    a = "ani"
    print ("selamat belajar " + a)

func()

print ("selamat belajar " + a)

