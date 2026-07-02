from tkinter import *
from tkinter import ttk

from shapes.rectagle import create_rectangle
from shapes.oval import create_oval
from shapes.circle import create_circle
from shapes.freehand import create_freehand
from shapes.line import create_line

# All figures
figures = []

# Create setup of screen


def setup(root):
    canvas = Canvas(root, bg='#101010', highlightthickness=0,
                    relief="flat", borderwidth=0)

    canvas.pack(fill="both", expand=True)

    # Create text of version

    def create_text_version():
        version = "1.0.0"
        version_label = Label(
            canvas,
            text=f"ProDraw @{version}",
            fg="#3F3F3F",
            bg="#101010",
            font=("Helvetica", 12, "bold")
        )
        version_label.place(relx=0, rely=1, x=30, y=-30, anchor="sw")

    # Create grid
    def create_grids(event=None):
        canvas.delete("grids")
        canvas.delete("version_text")

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        print(factor_zoom)

        # Adjust by zoom - Waiting for implement
        GRID_SIZE = 50

        for x in range(0, width, GRID_SIZE):
            for y in range(0, height, GRID_SIZE):
                canvas.create_oval(
                    x - 1, y - 1, x + 1, y + 1,
                    fill="#5B5B5B", outline="",
                    tags="grids",
                )

        canvas.tag_lower("grids")

        create_text_version()

    canvas.bind("<Configure>", create_grids)

    # Colors organized in 3 rows x 4 columns, matching the screenshot
    COLORS = [
        ["#FFFFFF", "#9398B0", "#E599F7", "#AE3EC9"],
        ["#4F72FC", "#4DABF7", "#FFC034", "#F76710"],
        ["#0B9268", "#40C057", "#FF8787", "#E03131"],
    ]

    PANEL_BG = "#1c1c22"
    SELECTED_BG = "#3a3a42"
    BUTTON_SIZE = 30

    # global state of the color picker
    canvas_by_color = {}
    selected_color_var = StringVar(value=COLORS[0][0])  # "#FFFFFF"

    # Criar panel of selection color
    def select_color(color):
        previous = selected_color_var.get()

        if previous in canvas_by_color:
            canvas_by_color[previous].config(bg=PANEL_BG)

        canvas_by_color[color].config(bg=SELECTED_BG)
        selected_color_var.set(color)

    # Create button colors
    def create_color_button(panel, row, column, color):
        cv = Canvas(
            panel, width=BUTTON_SIZE, height=BUTTON_SIZE,
            bg=PANEL_BG, highlightthickness=0, cursor="hand2"
        )
        cv.grid(row=row, column=column, padx=4, pady=4)

        cv.create_oval(6, 6, BUTTON_SIZE - 6, BUTTON_SIZE -
                       6, fill=color, outline="")
        cv.bind("<Button-1>", lambda e, c=color: select_color(c))

        canvas_by_color[color] = cv

        if color == selected_color_var.get():
            cv.config(bg=SELECTED_BG)

    # Create the color picker
    def create_color_picker(canvas):
        panel = Frame(canvas, bg=PANEL_BG, padx=12, pady=12)

        for row, row_colors in enumerate(COLORS):
            for column, color in enumerate(row_colors):
                create_color_button(panel, row, column, color)

        # pin to the top-right corner, with a 16px margin
        panel.place(relx=1.0, x=-16, y=16, anchor="ne")

    create_color_picker(canvas)
    select_color("#FFFFFF")

    # delete all draws in the screen

    def delete_all_draws():
        canvas.delete("rectangle")
        canvas.delete("oval")
        canvas.delete("circle")
        canvas.delete("line")
        canvas.delete("freehand")
        figures.clear()

    clear_button = ttk.Button(
        canvas, text="Limpar desenhos", command=delete_all_draws)
    clear_button.pack(side="bottom", anchor="se",
                      padx=30, pady=(0, 30), expand=False)

    draw_tools = {
        'Desenhar um:': None,
        'Quadrado': create_rectangle,
        'Círculo': create_circle,
        'Oval': create_oval,
        'Linha': create_line,
        'Mão livre': create_freehand
    }

    # Selection button

    def select_option_tool(option):
        draw_tools[option](
            canvas=canvas, bg=selected_color_var, figures=figures)

    menu_selected_option = StringVar()
    menu_selected_option.set(next(iter(draw_tools)))

    menu_tools = ttk.OptionMenu(canvas, menu_selected_option,
                                *draw_tools.keys(), command=select_option_tool)

    menu_tools.config(width=20)

    menu_tools.pack(side="bottom", anchor="se", padx=30, pady=10, expand=False)

    factor_zoom = 1.0
    ZOOM_STEP = 0.1
    ZOOM_MIN = 0.1
    ZOOM_MAX = 2

    def zoom(event):
        nonlocal factor_zoom

        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)

        if event.delta > 0:
            new_factor = min(round(factor_zoom + ZOOM_STEP, 1), ZOOM_MAX)
        else:
            new_factor = max(round(factor_zoom - ZOOM_STEP, 1), ZOOM_MIN)

        if new_factor == factor_zoom:
            return  # já está no limite, não faz nada

        # fator RELATIVO em relação ao estado atual do canvas
        scale_step = new_factor / factor_zoom
        canvas.scale("shape", x, y, scale_step, scale_step)
        # schedule_grid_update()

        factor_zoom = new_factor

    canvas.bind("<MouseWheel>", zoom)
