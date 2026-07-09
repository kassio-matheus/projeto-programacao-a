class DrawsModel:
    """Holds the figures dict and the shape tags used to clear the canvas."""

    SHAPE_TAGS = ["rectangle", "rectangle_preview", "oval", "oval_preview",
                  "circle", "circle_preview", "line", "line_preview",
                  "freedraw", "freedraw_preview"]

    def __init__(self, figures: dict):
        self.figures = figures
