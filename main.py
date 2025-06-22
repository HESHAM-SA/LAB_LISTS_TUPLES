avilebel_seat = []
booked_seat = []

for i in range(11):
    for j in range(21):
        avilebel_seat.append((i+1, j+1))


def check_availebel_seat(seat: tuple):
    if seat in booked_seat:
        print('The seat is booked')

    elif seat in avilebel_seat:
        print('The seat is availbel')
        user_input = int(input(f'Do you want to booked {seat}: '))
        print('1. Yes\n'
              '2. No')

        if user_input == 1:
            add_book_seat(seat)
        elif user_input == 2:
            pass

def add_book_seat(seat: tuple):
    if seat in avilebel_seat:
        booked_seat.append(seat)
        avilebel_seat.remove(seat)
        print(f'Your seat is booked, at {seat}')
    else:
        print(f'The {seat} is booked, please try other seat') 
        while True:
            row = int(input('Enter row'))
            col = int(input('Enter column'))
            add_book_seat((row, col))
            break             

def display_booked_seat():
    print('List of Booked Seats: ')
    booked_seat.sort()
    for i in booked_seat: # [(1,2),(1,1)]
        print(f'Row: {i[0]}, Seat: {i[1]}')

    Calculate_and_display()


def Calculate_and_display(): 
    print(f'Total booked seats is: {len(booked_seat)}')
    rows = [0] * 10
    for i in range(len(booked_seat)):
        seat = booked_seat[i][0] - 1
        rows[seat] = rows[seat] + 1

    for i in range(len(rows)):
        print(f'The row number {i + 1} has {rows[i]} booked seats')


def Cancel_booking(seat: tuple):
    if seat in booked_seat:
        booked_seat.remove(seat)
        avilebel_seat.append(seat)

    elif seat not in booked_seat:
        print(f'The seat: {seat} is not booked yet')






def display_list():
    while True:
        print('1. new book\n'
            '2. display booked seat\n'
            '3. display availabel seat\n' \
            '4. Check availabilit\n' \
            '5. Cancel booking\n'
            '6. Exit')
        user_input = int(input('Chose the number: '))

        if user_input == 1:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            add_book_seat((row, col))
            
        elif user_input == 2:
            display_booked_seat()

        elif user_input == 3:
            print(avilebel_seat)

        elif user_input == 4:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            check_availebel_seat((row, col))

        elif user_input == 5:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            Cancel_booking((row, col))
        
        elif user_input == 6:
            break



display_list()




