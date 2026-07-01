from tkinter import *
from abc import ABC, abstractmethod

#Faz a configuração da tela


class Screen(ABC):
    def __init__(self, canva: Canvas, window: Tk):
        self.canva = canva
        self.window = window

    @abstractmethod
    def create_draw(self):
        pass
