#  File: Queens.py
#  Description: This program solves the 8-queens problem by making recusion calls to place queens correctly
#  Student's Name: Marcos Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E
#  Unique Number: 51320
#
#  Date Created: 11/07/2016
#  Date Last Modified: 10/11/2016

import sys
sys.setrecursionlimit(10000)

class QueensProblem:
    # 1. Initialize queen board with all 0 to represent no queens
    def __init__(self, s):
        self.size = s
        self.solCount = 1
        self.board = [[0 for x in range(self.size)] for x in range(self.size)]

    # 2. Method that will call helper function to recursively solve diminishing board
    def solve(self,n):
        self.place_queen(0, 0)

    # 3. Method called by solve method that will repeatedly attempt to place
    #    queen in every column of every row
    def place_queen(self, row, column):
        """place a queen that satisfies all the conditions"""
        #base case
        if row > len(self.board)-1:
            print("Solution #", self.solCount)
            print(self)
            self.solCount += 1

        #check every column of the current row if its safe to place a queen
        while column < len(self.board):
            if self.isValidPlace(row, column):
                #place a queen
                self.board[row][column] = 1
                #place the next queen with an updated self.board
                return self.place_queen(row+1, 0)
            else:
                column += 1
        #there is no column that satisfies the conditions. Backtrack
        for c in range(len(self.board)):
            if self.board[row-1][c] == 1:
                #remove this queen
                self.board[row-1][c] = 0
                #go back to the previous row and start from the last unchecked column
                return self.place_queen(row-1, c+1)

    # 4. Method called to verify that no queens are in conflicting locations
    def isValidPlace(self, row, column):
        queens = []
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.board[r][c] == 1:
                    queen = (r,c)
                    queens.append(queen)
        for queen in queens:
            qr, qc = queen
            #check if the pos is in the same column or row
            if row == qr or column == qc:
                return False
            #check diagonals
            if (row + column) == (qr+qc) or (column-row) == (qc-qr):
                return False
        return True
        
    # Method that returns string representation of board
    def __str__(self):
        message = ""
        for i in range(len(self.board)):
            for j in self.board[i]:
                if j == 0:
                    message += ("*" + " ")
                else:
                    message += ("Q" + " ")
            message += "\n"
        return message

def main():
    num = 0
    # 1. Prompt user for input
    num = input("Enter board size: ")

    # 2. Determine if valid input and continue
    while num.isnumeric():
        num = int(num)
        print("\nNumber entered ", num)

        if num <= 3:
            print("Invalid input.")
        else:
            # 3. Create board
            print()
            board = QueensProblem(num)
            board.solve(num)

        num = input("Enter another board size (N to exit): ")

    # 3. End prgram
    print("Program ended.")

main()
