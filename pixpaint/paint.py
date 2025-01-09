import tkinter

class Paint(tkinter.Button):
	def __init__(self, parent, color, callback, *args, **kwargs):
		tkinter.Button.__init__(self, parent, bg=color, command=callback, highlightcolor=color, *args, **kwargs)
		self.parent = parent
