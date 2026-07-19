from tkinter import PhotoImage, Label, Canvas
from prodraw.models.workspace.logo_image_model import LogoImageModel


class LogoImageView:
    """Show logo image (ProDraw) in top side of workspace"""
    
    def __init__(self, canvas: Canvas, model: LogoImageModel):
        self.canvas = canvas
        self.model = model

    def render(self):
        image = PhotoImage(file=self.model.image)
        image_label = Label(self.canvas, image=image, bg=self.model.bg)
        image_label.pack(side="top", anchor="nw", padx=30, pady=30)
        image_label.image = image
