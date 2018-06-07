def board_draw(h , w):

    w+=1

    i=0
    for i in range(h):
        for j in range(w+w-1):
            print('-', end=""),
            j+=1
        print()
        for k in range(w+w-1):
            if k % 2 != 0:
                print(' ', end=""),
            else:
                print('|', end=""),
            k+=1
        i+=1

        print()
    for j in range(w + w - 1):
        print('-', end=""),
        j += 1


heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))
board_draw(heightinp,widthinp)