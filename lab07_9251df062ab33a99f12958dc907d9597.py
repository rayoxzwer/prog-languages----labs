from re import S
import time
from typing import List, Tuple, Generator


class Life:
    state: List[List[bool]]
    m: int
    n: int

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        
        self.state = []
        for i in range(m):
            my_list = []
            for j in range(n):
                my_list.append(False)
            self.state.append(my_list)

    def __repr__(self) -> str:
        return str(self.state)

    def neighbours(self, i: int, j: int) -> Generator[Tuple[int, int], None, None]:
        
        if ((i-1 >= 0 and i-1 < self.m) and (j >= 0 and j < self.n)):
            yield (i-1, j)
        if ((i+1 >= 0 and i+1 < self.m) and (j >= 0 and j < self.n)):
            yield (i+1, j)
        if ((i+1 >= 0 and i+1 < self.m) and (j+1 >= 0 and j+1 < self.n)):
            yield (i+1, j+1)
        if ((i-1 >= 0 and i-1 < self.m) and (j+1 >= 0 and j+1 < self.n)):
            yield (i-1, j+1)
        if ((i >= 0 and i < self.m) and (j-1 >= 0 and j-1 < self.n)):
            yield (i, j-1)
        if ((i >= 0 and i < self.m) and (j+1 >= 0 and j+1 < self.n)):
            yield (i, j+1)
        if ((i-1 >= 0 and i-1 < self.m) and (j-1 >= 0 and j-1 < self.n)):
            yield (i-1, j-1)
        if ((i+1 >= 0 and i+1 < self.m) and (j-1 >= 0 and j-1 < self.n)):
            yield (i+1, j-1)
        


    def nextstate(self) -> None:
        counter = 0
        next = []
        for i in range(0, self.m):
            temp = []
            for j in range(0, self.n):
                for pnt in self.neighbours(i, j):
                    if pnt == True:
                        counter += 1
                if counter == 2 or counter == 3:
                    temp.append(True)
            next.append(temp)
        self.state = next

    def addfigure(self, i: int, j: int, figure: List[str]) -> None:
        if i < 0 or j < 0 or i > self.m or j > self.n:
            raise ValueError("Incorrect values")
        a = 0
        for k in range(i, i + len(figure)):
            b = 0
            for l in range(j, j + len(figure[a])):
                if figure[a][b] == '#':
                    self.state[k][l] = True
                else:
                    self.state[k][l] = False
                b += 1
            a += 1        
                
    def __str__(self) -> str:
        empty = ""
        for i in range(0, self.m):
            for j in range(0, self.n):
                if self.state[i][j]:
                    empty = empty + "#"
                else:
                    empty += "."
            empty = empty + "\n"
        return empty

    
def start():

    toad = [".###",
            "###."]
    blinker = ["###"]

    block = ["..##..",
             "..##.."]
    
    glidergun = ["...................................#............",
                 ".................................#.#............",
                 ".......................##......##............##.",
                 "......................#...#....##............##.",
                 "...........##........#.....#...##...............",
                 "...........##........#...#.##....#.#............",
                 ".....................#.....#.......#............",
                 "......................#...#.....................",
                 ".......................##......................."]
    lf = Life(50, 80)
    lf. addfigure(10, 10, glidergun)
    lf. addfigure(30, 10, toad)
    lf. addfigure(40, 15, blinker)
    lf. addfigure(20, 60, block)
    
    while True:
        print(lf)
        print("press Ctrl-C to stop")
        lf. nextstate()
        time. sleep(0.25)
start()
