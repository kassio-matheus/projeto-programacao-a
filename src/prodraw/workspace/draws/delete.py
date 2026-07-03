class Delete:
    """Handles the removal of all drawn shapes from the canvas."""
    
    # Initializes the delete handler with the target canvas and figures list
    def __init__(self, canvas, figures):
        self.canvas = canvas
        self.figures = figures
        pass

    # Clears all shape tags from the canvas and empties the stored figures list
    def delete_all_draws(self):
        self.canvas.delete("rectangle")
        self.canvas.delete("oval")
        self.canvas.delete("circle")
        self.canvas.delete("line")
        self.canvas.delete("freehand")
        self.figures.clear()