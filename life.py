import time, sys

SIZE = int(sys.argv[1])
stable = False

def read_coord(live):
    num = int(raw_input('Enter the number:'))
    for i in range(num):
        input = raw_input('-').split()
        x = int(input[0])
        y = int(input[1])
        live.append([x, y])


def num_of_neighbours(live, cell):
    x,y = cell
    neighbours = 0
    for i in range(3):
        if [x - 1, y - 1 + i] in live:
            neighbours += 1
        if [x + 1, y - 1 + i] in live:
            neighbours += 1
    if [x, y - 1] in live:
        neighbours += 1
    if [x, y + 1] in live:
        neighbours += 1
    return neighbours


def update(live):
    global stable
    
    dead_cells = []
    new_cells = []
    
    for i in range(SIZE):
        for j in range(SIZE):
            n = num_of_neighbours(live, [i, j])
            if [i, j] in live:
                if n < 2 or n > 3:
                    dead_cells.append([i, j])
            else:
                if n == 3:
                    new_cells.append([i, j])

    if dead_cells or new_cells:
        for cell in dead_cells:
            live.remove(cell)
        for cell in new_cells:
            live.append(cell)
    else:
        stable = True 


def show(live):
    for i in range(SIZE):
        for j in range(SIZE):
            if [i, j] in live:
                print 'O ',
            else:
                print '. ',
        print 
        print



def main():
    day = 0

    live = []

    read_coord(live)

    while live and not stable:

        day += 1
        print 'day', day
        show(live)
        print '\n\n'

        update(live)

        time.sleep(1)

    day += 1
    print 'day', day
    show(live)

if __name__ == '__main__':
    main()
