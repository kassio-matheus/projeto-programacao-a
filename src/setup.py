from tkinter import *
from tkinter import ttk

from examples.rectagle import Rectangle
from examples.ovals import Oval


def setup(root):
    figuras = []
    canvas = Canvas(root, bg='black', highlightthickness=0,
                    relief="flat", borderwidth=0)

    canvas.pack(fill="both", expand=True)

    def create_text_version():
        version = "1.0.0"
        canvas.create_text(
            30, canvas.winfo_height() - 30,
            anchor="sw",
            fill="white",
            font=("Helvetica", 12, "bold"),
            text=f"ProDraw @{version}",
            tags="version_text"
        )

    def create_grids(event=None):
        canvas.delete("grids")
        canvas.delete("version_text")

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

        create_text_version()

    canvas.bind("<Configure>", create_grids)

    # frame_tools = Frame(root, width=50, height=50, bg="black")
    # frame_tools.pack(side="right", fill="x", padx=20, pady=20)

    def delete_all_draws():
        canvas.delete('oval')
        canvas.delete('rectangle')
        figuras.clear()
        pass

    clear_button = ttk.Button(
        canvas, text="Limpar desenhos", command=delete_all_draws)
    clear_button.pack(side="bottom", anchor="se",
                      padx=30, pady=(0, 30), expand=False)

    draw_tools = {
        'Selecione uma opção': None,
        'Desenhar um retangulo': Rectangle,
        'Desenhar um oval': Oval
    }

    def select_option_tool(option):
        draw_tools[option](canvas, figuras)

    menu_selected_option = StringVar()
    menu_selected_option.set(next(iter(draw_tools)))

    menu_tools = ttk.OptionMenu(canvas, menu_selected_option,
                                *draw_tools.keys(), command=select_option_tool)

    menu_tools.config(width=20)

    menu_tools.pack(side="bottom", anchor="se", padx=30, pady=10, expand=False)
