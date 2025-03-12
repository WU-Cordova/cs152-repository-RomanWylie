from projects.project2.cell import Cell
from datastructures.array2d import Array2D
from random import randint
from copy import deepcopy


class Grid:
    def __init__(self, rows:int = 10, cols:int = 10):
        self.__rows=rows
        self.__cols=cols
        self.grid = Array2D.empty(rows=rows, cols=cols, data_type=Cell)
        self.history = []

    def first_generation(self):
        for y in range(self.__rows):
            for x in range(self.__cols):
                seed = randint(1,2)
                if seed == 2:
                    self.grid[y][x].alive = True
                else:
                    pass
            


    def check_neighbors(self, row_index: int, col_index:int):
        cell_to_check=self.grid[row_index][col_index]
        rows_range = [row_index-1, row_index+2]
        cols_range = [col_index-1, col_index+2]
        neighbor_count=0
        for y in range(rows_range[0], rows_range[1]):
            if y in range(self.__rows): 
                for x in range(cols_range[0], cols_range[1]):
                    if x in range(self.__cols) and (x,y) !=(col_index,row_index):
                        if self.grid[y][x].isalive():
                            neighbor_count+=1
            
        return neighbor_count
    
    def generate_next_grid(self):
        self.next_gen = Array2D.empty(rows=self.__rows, cols=self.__cols, data_type=Cell)
        for y in range(self.__rows):
            for x in range(self.__cols):
                neighbors = self.check_neighbors(row_index=y,col_index=x)
                match neighbors:
                    case 0|1:
                        self.next_gen[y][x].alive = False
                    case 2:
                        self.next_gen[y][x].alive = self.grid[y][x].alive
                    case 3:
                        self.next_gen[y][x].alive = True
                    case 4|5|6|7|8:
                        self.next_gen[y][x].alive = False
        if len(self.history) >= 3:
            self.history.pop(0)
        self.history.append(deepcopy(self.grid))
        self.grid = deepcopy(self.next_gen)

    def repeating_grids(self):
        if any(str(self.grid)==str(x) for x in self.history):
            return True

    def __str__(self):
        return f' {" ".join(f"{str(row)}\n" for row in self.grid)}'
    
        


                        
      
        

