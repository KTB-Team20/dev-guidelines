def print_pyramid(height):
    for i in range(height):
        print(' ' * (height - i - 1), end='')

        print('*' * (2 * i + 1))

height = int(input("이게 뭘까? : "))
print_pyramid(height)
