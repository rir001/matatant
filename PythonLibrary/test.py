from matatant import Matatant

matata = Matatant(8)

run = 1
while run:
    option = input('option: ')
    if option == 'q':
        matata.write(str.encode(f'!'))
        matata.close()
        run = 0

    elif option == 'f':
        matata.forward(int(input('forward: ')))

    elif option == 'l':
        matata.left(int(input('left: ')))

    elif option == 'r':
        matata.right(int(input('right: ')))




