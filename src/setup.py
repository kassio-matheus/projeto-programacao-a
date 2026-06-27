from tkinter import *


def setup(root):
    canvas = Canvas(root, bg='black', highlightthickness=0,
                    relief="flat", borderwidth=0)
    
    canvas.pack(fill="both", expand=True)

    def create_grids(event=None):
        canvas.delete("grids")

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        # Adjust by zoom - Waiting for implement
        GRID_SIZE = 20

        for x in range(0, width, GRID_SIZE):
            for y in range(0, height, GRID_SIZE):
                canvas.create_oval(
                    x - 1, y - 1, x + 1, y + 1,
                    fill="#3a3a3a", outline="",
                    tags="grids",
                )

        canvas.tag_lower("grids")

    canvas.bind("<Configure>", create_grids)

    # frame_tools = Frame(master=root, width=50, height=50, bg="red")
    # frame_tools.pack(side="bottom", fill="x")
