print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("So, you're %s old, %s tall and %s heavy."%(age, height, weight))

from sys import argv
script, filename = argv

txt = open(filename)

print("Here's your file %s:"%filename)
print(txt.read())

print("Type the filename again:",end=' ')
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


print("Let's practice everything.")
print('You\'d need to know \'bout escapes \n with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print("This should be five: %s."%five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars * 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: %s."%start_point)
# it's just like with an f"" string
print("We'd have %s beans, %s jars, and %s crates."%(beans, jars, crates))

startpoint = start_point / 10

print("We can also do that this way:")
beans, jars, crates = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have %s beans, %s jars, and %s crates."%(beans, jars, crates))



people = 20
cates = 30
dogs = 15


if people < cates:
    print("Too many cats! The world is doomed!")

if people < cates:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

