import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

symbol_value = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_winnings(columns,lines, bet,values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning_line.append(line +  1)
            winnings += values[symbol] * bet
    
    return winnings,winning_line


def get_slot_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)    
    
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=' | ')
            else:
                print(column[row],end='')
        
        print()

def deposit():
    while True:
        amount = input('What would you like to deposit? $ ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print('Amount must be greater than 0')
        else:
            print('Please enter a number')

    return amount

def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES})? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print('Enter Valid number of lines')
        else:
            print('Please enter a number')

    return lines

def get_bet():
    while True:
        bet = input(f'How much would you like to bet on each line? ')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else: 
                print(f'Amount must be between ${MIN_BET} and ${MAX_BET}')
        else:
            print('Please enter a number')

    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You do not have enough to bet that amount. Your balance is {balance}')
        else:
            break

    print(f'You\'re betting ${bet} on {lines} lines. Total bet amount is {total_bet}')

    slots = get_slot_spin(ROWS,COLS,symbol_count)
    print_slot(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f'You won {winnings}')
    print('Lines won', *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer =  input('Press Enter to spin (q to quit)')
        if answer == 'q':
            break
        balance += spin(balance)
    print (f'You left with {balance}')
main()