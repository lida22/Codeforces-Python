number = input()
def cube(number):
    print number**3
def by_three(number):
    if number%3 == 0:
        print cube(number)
    else:
        return False
