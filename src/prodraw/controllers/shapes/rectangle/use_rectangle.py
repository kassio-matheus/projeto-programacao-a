from tkinter import Canvas, StringVar

from .rectangle_controller import RectangleController
from prodraw.models.shapes import Rectangle


def rectangle_bind(canvas: Canvas, figures: dict, bg: StringVar) -> RectangleController:
    controller = RectangleController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def rectangle_sync_data(canvas: Canvas, figures: list, data: list) -> RectangleController:
    # Instancia o controller para ter acesso à view e à lista de figuras
    # Passamos um lambda vazio para o get_bg já que não vamos desenhar manualmente agora
    controller = RectangleController(canvas, figures, get_bg=lambda: "#000000")

    for rect_tuple in data:
        # Cria o objeto Rectangle passando os dados desempacotados da tupla
        rectangle = Rectangle(*rect_tuple)

        # Sincroniza com o dicionário de figuras do sistema
        controller.figures['Rectangle'].append(rectangle.to_tuple())

        # Desenha o retângulo definitivo no Canvas utilizando os dados salvos
        controller.view.draw(*rect_tuple)

    return controller


def rectangle_delete(canvas: Canvas, controller: RectangleController):
    controller.unbind()
