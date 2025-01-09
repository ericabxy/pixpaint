#!/usr/bin/env python
import os
import sys
import tkinter as tk

from pixpaint import cga
from PIL import Image, ImageDraw

class Brush():
	def __init__(self):
		return None


class Canvas(tk.Canvas):
	def __init__(self, parent, *args, **kwargs):
		tk.Canvas.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.bind("<Button-1>", self.click)

	def click(self, event):
		self.create_rectangle(event.x, event.y, event.x, event.y)


class Application(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.canvas = Canvas(self, bg="magenta").pack()
		self.palette = cga.Palette(self).pack()


if __name__ == "__main__":
	window = tk.Tk()
	window.geometry("640x480")
	window.title("Pillow")
	Application(window).pack(side="top", fill="both", expand=True)
	window.mainloop()
