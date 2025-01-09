import tkinter

from .paint import Paint

class Palette(tkinter.Frame):
	def __init__(self, parent, *args, **kwargs):
		tkinter.Frame.__init__(self, parent, *args, **kwargs)
		self.paints = (
			Paint(self, "#000000", lambda: self.dip(( 0, 0, 0 ))),
			Paint(self, "#0000AA", lambda: self.dip(( 0, 0, 170 ))),
			Paint(self, "#00AA00", lambda: self.dip(( 0, 170, 0 ))),
			Paint(self, "#00AAAA", lambda: self.dip(( 0, 170, 170 ))),
			Paint(self, "#AA0000", lambda: self.dip(( 170, 0, 0 ))),
			Paint(self, "#AA00AA", lambda: self.dip(( 170, 0, 170 ))),
			Paint(self, "#AA5500", lambda: self.dip(( 170, 85, 0 ))),
			Paint(self, "#AAAAAA", lambda: self.dip(( 170, 170, 170 ))),
			Paint(self, "#555555", lambda: self.dip(( 85, 85, 85 ))),
			Paint(self, "#5555FF", lambda: self.dip(( 85, 85, 255 ))),
			Paint(self, "#55FF55", lambda: self.dip(( 85, 255, 85 ))),
			Paint(self, "#55FFFF", lambda: self.dip(( 85, 255, 255 ))),
			Paint(self, "#FF5555", lambda: self.dip(( 255, 85, 85 ))),
			Paint(self, "#FF55FF", lambda: self.dip(( 255, 85, 255 ))),
			Paint(self, "#FFFF55", lambda: self.dip(( 255, 255, 85 ))),
			Paint(self, "#FFFFFF", lambda: self.dip(( 255, 255, 255 )))
		)
		for paint in self.paints:
			paint.pack(side="left")
	
	def dip(self, color):
		self.color = color
		print(color, self.color)
