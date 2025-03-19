class Line():
    
    def __init__(self, a, b):
        #a and b are points
        self.a = a
        self.b = b

        self.x1 = self.a.x
        self.y1 = self.a.y
        self.x2 = self.b.x
        self.y2 = self.b.y
    
    def draw(self, canvas, color="black"):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=color, width = 2)