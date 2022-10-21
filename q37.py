class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    key = board[i][j]
                    rows[i].add(key)
                    columns[j].add(key)
                    boxs[(i//3)*3 + (j//3)].add(key)

        def recursion(i,j):
            if j > 8:
                j = 0
                i += 1
            if i > 8 and i > 8:
                return True

            if board[i][j] != '.':
                return recursion(i,j+1)
            else:
                poss_choice = []

                for choice in range(1,10):
                    choice = str(choice)
                    if choice not in rows[i] and choice not in columns[j] and choice not in boxs[(i//3)*3 + (j//3)]:
                        poss_choice.append(choice)

                for poss in poss_choice:
                    rows[i].add(poss)
                    columns[j].add(poss)
                    boxs[(i // 3) * 3 + (j // 3)].add(poss)
                    board[i][j] = poss
                    correct = recursion(i,j+1)
                    if correct:
                        return True
                    else:
                        rows[i].remove(poss)
                        columns[j].remove(poss)
                        boxs[(i // 3) * 3 + (j // 3)].remove(poss)
                        board[i][j] = '.'

        recursion(0,0)
