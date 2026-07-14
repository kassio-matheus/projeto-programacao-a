from tkinter import Canvas, Tk, filedialog, messagebox
import pickle

# Config imports
from prodraw.config import WORKSPACE_COLORS

# Controllers
from prodraw.controllers.window import WindowController
from prodraw.controllers.workspace.color_picker_controller import ColorPickerController
from prodraw.controllers.workspace.grids_controller import GridsController
from prodraw.controllers.workspace.clear_draws_controller import ClearDrawsController
from prodraw.controllers.workspace.tools_controller import ToolsController
from prodraw.controllers.workspace.zoom_controller import ZoomController
from prodraw.controllers.workspace.logo_image_controller import LogoImageController
from prodraw.controllers.workspace.cursor_controller import CursorController

# Sync data functions controllers - Load file .pickle
from prodraw.controllers.shapes.rectangle import rectangle_sync_data
from prodraw.controllers.shapes.oval import oval_sync_data
from prodraw.controllers.shapes.line import line_sync_data
from prodraw.controllers.shapes.circle import circle_sync_data
from prodraw.controllers.shapes.freedraw import freedraw_sync_data
from prodraw.controllers.shapes.square import square_sync_data


class Workspace:
    """Main workspace — wires up all MVC components."""

    def __init__(self, root: Tk, version, window: WindowController):
        self.root = root
        self.bg = WORKSPACE_COLORS.get("bg")

        self.canvas = Canvas(root, bg=self.bg, highlightthickness=0,
                             relief="flat", borderwidth=0)

        # figures dict matches the shape keys used by shape controllers
        self.figures = {
            'Circle': [], 'Rectangle': [],
            'Oval': [], 'Line': [], 'FreeDraw': [], 'Square': []
        }

        self.version = version
        self.window = window

    def save_file(self, files):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".prodraw",
            filetypes=[("Arquivos ProDraw", "*.prodraw"),
                       ("Todos os arquivos", "*.*")],
            title="Escolha onde salvar seus dados",
        )

        if file_path:
            try:
                with open(file_path, "wb") as arquivo:
                    pickle.dump(files, arquivo)
                messagebox.showinfo(
                    "Sucesso", "Todos os seus dados foram salvos com sucesso!")
            except Exception as e:
                messagebox.showerror(
                    "Erro", f"Não foi possível salvar: \n{e}")

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos ProDraw", "*.prodraw"),
                       ("Todos os arquivos", "*.*")],
            title="Selecione o arquivo para carregar",
        )

        if file_path:
            try:
                with open(file_path, "rb") as arquivo:
                    loaded_data = pickle.load(arquivo)

                    self.canvas.delete("shape")

                    for figure in loaded_data:
                        figures_loaded = loaded_data[figure]
                        self.figures[figure] = figures_loaded

                        for data in figures_loaded:
                            if figure == "Rectangle":
                                rectangle_sync_data(
                                    self.canvas, figures=self.figures, data=data)
                            elif figure == "Circle":
                                circle_sync_data(
                                    self.canvas, figures=self.figures, data=data)
                            elif figure == "Oval":
                                oval_sync_data(
                                    self.canvas, figures=self.figures, data=data)
                            elif figure == "Line":
                                line_sync_data(
                                    self.canvas, figures=self.figures, data=data)
                            elif figure == "FreeDraw":
                                freedraw_sync_data(
                                    self.canvas, figures=self.figures, data=data)
                            elif figure == "Square":
                                square_sync_data(
                                    self.canvas, figures=self.figures, data=data)

                messagebox.showinfo(
                    "Dados carregados", "Os seus dados foram importados com sucesso na sua área de trabalho."
                )
            except Exception as e:
                print(e)

    def start(self):
        self.canvas.pack(fill="both", expand=True)

        # Load or save file in menubar -> Waiting for create in MVC

        self.window.update_menu(isSubItem=True, subItem="Arquivo",
                                label="Exportar workspace", command=lambda: self.save_file(self.figures))

        self.window.update_menu(isSubItem=True, subItem="Arquivo",
                                label="Importar workspace", command=self.load_file)

        # Dot grid — redraws on every canvas resize
        grid_ctrl = GridsController(self.canvas, self.version)
        self.canvas.bind("<Configure>", grid_ctrl.on_resize)

        # Logo image - Top side on left
        logo_image = LogoImageController(
            self.canvas, "public/icons/logo.png", self.bg)
        logo_image.setup()

        color_ctrl = ColorPickerController(self.canvas)
        selected_color_var = color_ctrl.setup()

        ClearDrawsController(self.canvas, self.figures,
                            window=self.window, subItemMenu="Arquivo").setup()

        toolsbar = ToolsController(self.canvas, selected_color_var, self.figures, window=self.window)
        toolsbar.setup()

        color_ctrl.cursor = toolsbar.cursor

        # Scroll-to-zoom
        zoom_ctrl = ZoomController(self.canvas, window=self.window)
        zoom_ctrl.setup()
