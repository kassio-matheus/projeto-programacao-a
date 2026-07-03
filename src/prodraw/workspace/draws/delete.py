class Delete:
    def __init__(self, canvas, figures):
        self.canvas = canvas
        self.figures = figures
        pass

    def delete_all_draws(self):
        self.canvas.delete("rectangle")
        self.canvas.delete("oval")
        self.canvas.delete("circle")
        self.canvas.delete("line")
        self.canvas.delete("freehand")
        self.figures.clear()
