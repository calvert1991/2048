"""
    2048 code written by Cachen

    2015年 11月 13日 星期五 13:30:58 CST
    2015年 11月 13日 星期五 21:36:36 CST
    2015年 11月 14日 星期六 10:41:06 CST
    2015年 11月 14日 星期六 11:46:04 CST
    2015年 11月 14日 星期六 13:13:05 CST
"""
import random

def getchar(matrix):
    direction = input("input direction: w, UP; s, Down; d, Right; a, Left   ")
    list_row = []
    list_coloumn = []
    """
    the following code is combining move and merge for four direction
    """
    if direction == "a":
        row = 0
        coloumn = 0
        while row < 4:
            # list_row[row] = []
            list_row.append([])
            while coloumn < 4:
                if matrix[row][coloumn] != 0:
                    list_row[row].append(matrix[row][coloumn])
                coloumn += 1
            # print("list_row = ", list_row[row])
            count = 0
            while len(list_row[row]) >= 2:
                if list_row[row][0] == list_row[row][1]:
                    matrix[row][count] = list_row[row][0] * 2
                    list_row[row].pop(0)
                    # list_row[row].pop(1)
                    list_row[row].pop(0)
                    count += 1
                else:
                    matrix[row][count] = list_row[row][0]
                    list_row[row].pop(0)
                    count += 1
            if len(list_row[row]) > 0:
                matrix[row][count] = list_row[row][0]
                count += 1
            for left in range(count, 4):
                matrix[row][left] = 0
            coloumn = 0
            row += 1
    elif direction == "d":
        row = 0
        coloumn = 3
        while row < 4:
            list_row.append([])
            while coloumn >= 0:
                if matrix[row][coloumn] != 0:
                    list_row[row].append(matrix[row][coloumn])
                coloumn -= 1
            count = 3
            while len(list_row[row]) >= 2:
                if list_row[row][0] == list_row[row][1]:
                    matrix[row][count] = list_row[row][0] * 2
                    list_row[row].pop(0)
                    list_row[row].pop(0)
                    count -= 1
                else:
                    matrix[row][count] = list_row[row][0]
                    list_row[row].pop(0)
                    count -= 1
            if len(list_row[row]) > 0:
                matrix[row][count] = list_row[row][0]
                count -= 1
            for left in range(count, -1, -1):
                matrix[row][left] = 0
            coloumn = 3
            row += 1
    elif direction == "w":
        coloumn = 0
        row = 0
        while coloumn < 4:
            list_coloumn.append([])
            while row < 4:
                if matrix[row][coloumn] != 0:
                    list_coloumn[coloumn].append(matrix[row][coloumn])
                row += 1
            # print(list_coloumn[coloumn])
            count = 0
            while len(list_coloumn[coloumn]) >= 2:
                if list_coloumn[coloumn][0] == list_coloumn[coloumn][1]:
                    matrix[count][coloumn] = list_coloumn[coloumn][0] * 2
                    list_coloumn[coloumn].pop(0)
                    list_coloumn[coloumn].pop(0)
                    count += 1
                else:
                    matrix[count][coloumn] = list_coloumn[coloumn][0]
                    list_coloumn[coloumn].pop(0)
                    count += 1
            if len(list_coloumn[coloumn]) > 0:
                matrix[count][coloumn] = list_coloumn[coloumn][0]
                count += 1
            for left in range(count, 4):
                matrix[left][coloumn] = 0
            row = 0
            coloumn += 1
    elif direction == "s":
        coloumn = 0
        row = 3
        while coloumn < 4:
            list_coloumn.append([])
            while row >= 0:
                if matrix[row][coloumn] != 0:
                    list_coloumn[coloumn].append(matrix[row][coloumn])
                row -= 1
            count = 3
            while len(list_coloumn[coloumn]) >= 2:
                if list_coloumn[coloumn][0] == list_coloumn[coloumn][1]:
                    matrix[count][coloumn] = list_coloumn[coloumn][0] * 2
                    list_coloumn[coloumn].pop(0)
                    list_coloumn[coloumn].pop(0)
                    count -= 1
                else:
                    matrix[count][coloumn] = list_coloumn[coloumn][0]
                    list_coloumn[coloumn].pop(0)
                    count -= 1
            if len(list_coloumn[coloumn]) > 0:
                matrix[count][coloumn] = list_coloumn[coloumn][0]
                count -= 1
            for left in range(count, -1, -1):
                matrix[left][coloumn] = 0
            row = 3
            coloumn += 1




"""
bug look like:
input direction: w, UP; s, Down; d, Right; a, Left   a
[8, 4, 0, 0]
[4, 2, 0, 0]
[8, 2, 0, 2]
[4, 2, 0, 0]
input direction: w, UP; s, Down; d, Right; a, Left   a
Game is over
"""

# fill of bugs, Fix me
def isOver(matrix):  ## Need fix the magic number
    ExistZero = True ## the matrix exist zero items
    for row in range(0,4): # not the range(0,3)
        # if matrix[row].count(0) != 0:
        for coloumn in range(0,4):
            if matrix[row][coloumn] == 0:
                ExistZero = True
                break
        ExistZero = False

    if ExistZero == False:
        for row in range(0,3):
            for coloumn in range(0,3):
                if matrix[row][coloumn] == matrix[row][coloumn+1]:
                    return False
                if matrix[row][coloumn] == matrix[row+1][coloumn]:
                    return False
            if matrix[0][3] == matrix[1][3]:
                return False
        for num in range(0,2):
            if matrix[3][num] == matrix[3][num+1]:
                return False
        return True
    else: return False


def insert(matrix):
    # ExistZero = True ## the matrix exist zero items
    # for row in range(0,4): # not the range(0,3)
        # for coloumn in range(0,4):
            # if matrix[row][coloumn] == 0:
                # ExistZero = True
                # break
            # ExistZero = False
    # if ExistZero == False:
        # return None
    x = random.randint(0,3)
    y = random.randint(0,3)
    while matrix[x][y] != 0: ## 如何数组满了的话，这个不就是死循环了吗
        x = random.randint(0,3)
        y = random.randint(0,3)
    matrix[x][y] = 2

def display(matrix):
    for row in range(0,4):
        print(matrix[row])

def play():
    """
    using tuple is error
    the item of tuple can't change
    """
    matrix = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    x1 = random.randint(0,3)
    y1 = random.randint(0,3)
    matrix[x1][y1] = 2

    x2 = random.randint(0,3)
    y2 = random.randint(0,3)
    while matrix[x2][y2] == 2:
        x2 = random.randint(0,3)
        y2 = random.randint(0,3)

    matrix[x2][y2] = 2

    # print(matrix)
    while not isOver(matrix):
        display(matrix)
        getchar(matrix)
        insert(matrix)

    print("Game is over")

play()











