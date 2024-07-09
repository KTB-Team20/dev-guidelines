def print_pyramid(height):
    for i in range(height):
        print(' ' * (height - i - 1), end='')

        print('*' * (2 * i + 1))
        
# 출력할 피라미드의 높이를 입력하는 값
height = int(input("출력할 피라미드이 높이 : "))
print_pyramid(height)
