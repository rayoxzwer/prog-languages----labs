def sine(x):
    n = 50
    result = 0
    power = 1
    drv = -1
    for i in range(1, n):
        power = power * x
        if i % 2 != 0:
            fact = 1
            drv = drv * (-1)
            for j in range(1, i+1):
                fact = fact * j
            result += power * drv/fact
    return result

print(sine( 0.1 ))
print(sine( 30 * 3.1415926536 / 180 ))
print(sine( 0.5 - 0.3j ))
print(sine( 1 ))
print(sine( 0.6 ))
print(sine( 0.8 ))

def collatz():
    try:
        inp = input("Please type a number greater than one or ’quit’ to quit: ")
        if inp == 'quit' or inp == 'q':
            print("Goodbye!")
            exit()
        i = int(inp)
        while True:
            if i <= 1:
                print("You typed 1 or negative number, which is not greater than 1")
                inp = input("Please type a number greater than one or ’quit’ to quit: ")
                if inp == 'quit' or inp == 'q' or inp == 'Q':
                    print("goodbye")
                    exit()
                i = int(inp)
            else:
                print(f"Giving Collatz sequence for {i}")
                it = 1
                j = i
                print(f"iteration {it} results in {j}")
                while j != 1:
                    if j % 2 == 0:
                        it = it + 1
                        j = j // 2
                        print(f"iteration {it} results in {j}")
                    elif j % 2 == 1:
                        it = it + 1
                        j = 3 * j + 1
                        print(f"iteration {it} results in {j}")
                inp = input("Please type a number greater than one or ’quit’ to quit: ")
                if inp == 'quit' or inp == 'q' or inp == 'Q':
                    print("goodbye")
                    exit()
                i = int(inp)
    except ValueError:
        print("ValueError!")
collatz()
