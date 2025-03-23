from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        try:
            self._create_cells()
            self._break_entrance_and_exit()
        except AttributeError as e:
            print(f"AttributeError: {e}")
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
        
        self._break_entrance_and_exit()
        
    
    def _draw_cell(self,i,j):
        x_pos = self.x1 + (i * self.cell_size_x)
        y_pos = self.y1 + (j * self.cell_size_y)

        cell = self._cells[i][j]

        cell.draw(x_pos, y_pos, x_pos + self.cell_size_x, y_pos + self.cell_size_y)
        
        try:
            self._animate()
        except Exception as e:
            print(f"Error! {e}")
            
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        #identiy the first and last cell
        first_cell = self._cells[0][0]
        last_cell = self._cells[self.num_cols-1][self.num_rows-1]

        #remove the top of the first cell and bottom of the last cell
        first_cell.has_top_wall = False
        self._draw_cell(0,0)
        last_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)
        return