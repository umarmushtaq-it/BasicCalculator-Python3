

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def subs(self):
        return float(self.x - self.y)

    def add(self):
        return float(self.x + self.y)

    def mul(self):
        return float(self.x * self.y)

    def div(self):
        return float(self.x / self.y)

    def square(self):
        return float(self.x*self.x)

    def average(self):
        z=0
        for i in range(len(self.y)):
            z=z+self.y[i]
        return float(z/len(self.y))


while True:
    user_input = input("""Choose Operation:
                  1 = Addition
                  2 = Subtraction
                  3 = Multiplication
                  4 = Division
                  5 = Square
                  6 = Average
                  In order to exit, type 'Quit'. Enter choice:""")
    if user_input == '1':
        while True:
            try:
                first_num=float(input('Enter the first number you want to add:'))
            except ValueError:
                print('Invalid input. Please try again')
                continue
            while True:
                try:
                    second_num =float(input('Now enter the second number to add:'))
                except ValueError:
                    print('Invalid input. Please try again')
                    continue
                values=Calculator(first_num,second_num)
                print('Result = {:.2f}'.format(values.add()))
                break
            break

    elif user_input == '2':
        while True:
            try:
                first_num = float(input('Enter the first number you want to substract:'))
            except ValueError:
                print('Invalid input. Please try again')
                continue
            while True:
                try:
                    second_num = float(input('Now enter the second number to substract:'))
                except ValueError:
                    print('Invalid input. Please try again')
                    continue
                values = Calculator(first_num, second_num)
                print('Result = {:.2f}'.format(values.subs()))
                break
            break

    elif user_input == '3':
        while True:
            try:
                first_num = float(input('Enter the first number you want to multiply:'))
            except ValueError:
                print('Invalid input. Please try again')
                continue
            while True:
                try:
                    second_num = float(input('Now enter the second number to multiply:'))
                except ValueError:
                    print('Invalid input. Please try again')
                    continue
                values = Calculator(first_num, second_num)
                print('Result = {:.2f}'.format(values.mul()))
                break
            break

    elif user_input == '4':
        while True:
            try:
                first_num = float(input('Enter the first number you want to divide:'))
            except ValueError:
                print('Invalid input. Please try again')
                continue
            while True:
                try:
                    second_num = float(input('Now enter the second number to divide:'))
                except ValueError:
                    print('Invalid input. Please try again')
                    continue
                values = Calculator(first_num, second_num)
                print('Result = {:.2f}'.format(values.div()))
                break
            break

    elif user_input == '5':
        while True:
            try:
                first_num = float(input('Enter the first number you want to square:'))
            except ValueError:
                print('Invalid input. Please try again')
                continue
            second_num=0
            values = Calculator(first_num, second_num)
            print('Result = {:.2f}'.format(values.square()))
            break

    elif user_input == '6':
        num_list = []
        while True:
            try:
                iterator = int(input('How many numbers you want to calculate the average of'))
            except ValueError:
                print('Invalid input. Please try again')
                continue
            while True:
                try:
                    for i in range(iterator):
                        asknumbers= float(input('Now enter number {}:'.format(i+1)))
                        num_list.append(asknumbers)
                except ValueError:
                    print('Invalid input. Please try again')
                    continue
                values = Calculator(iterator, num_list)
                print('Result = {:.2f}'.format(values.average()))
                break
            break

    elif user_input == ('Quit') or user_input == ('quit'):
        break

    else:
        print('Invalid input. Please try again')