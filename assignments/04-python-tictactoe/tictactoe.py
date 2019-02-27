#!/usr/bin/env python3
"""docstring"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--state', help='Board state',
                        metavar='str', type=str, default='.........')
    parser.add_argument('-p', '--player', help='Player',
                        metavar='str', type=str, default='')
    parser.add_argument('-c', '--cell', help='Cell to apply -p', 
                        metavar='int', type=int)
    return parser.parse_args()

# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    state = args.state
    cell = args.cell
    player = args.player
    #print(args)
 
    if player and player not in 'XO':
        print('Invalid player "{}", must be X or O'.format(player))
        sys.exit(1)

    for i in state:
        if(i !="X" and i != "O" and i != "."):  
            print('Invalid state "{}", must be 9 characters of only ., X, O'.format(state))
            sys.exit(1)
    
    if len(state) != 9: 
        print('Invalid state "{}", must be 9 characters of only ., X, O'.format(state))
        sys.exit(1) 

    if cell is not None and not 1 <= cell <= 9: 
        print('Invalid cell "{}", must be 1-9'.format(cell))
        sys.exit(1) 

    for i, c in enumerate(state):
        cell_int = i+1
        if cell_int == cell and c in 'XO' and player not in '': 
            print("Cell {} already taken".format(cell)) 
            sys.exit(1)

    if player not in '':
        cell_sub = player
    else:
        cell_sub = cell 
    if not cell and player:
        print("Must provide both --player and --cell")
        sys.exit(1)    
    if cell and not player:
        print("Must provide both --player and --cell")
        sys.exit(1)     

    bar = "-------------"
    print(bar) 

    for i, c in enumerate(state): 
        cell_val = i + 1 if c == '.' else c
        if cell_val == cell:
            print("| {} ".format(cell_sub), end='') 
        else:
            print("| {} ".format(cell_val), end='')
        if (i + 1) % 3 == 0: 
            print("|") 
            print(bar)
# --------------------------------------------------
if __name__ == '__main__':
    main()
