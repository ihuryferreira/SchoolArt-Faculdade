"""
ttips.py module

original tooltip class source:
https://www.daniweb.com/programming/software-development/code/484591/
a-tooltip-class-for-tkinter

v06 added try accept at end as occasional unknown error
    I can't work out what exception error namr to use omn it.
v05 added these parameters :bgcolor, fgcolor, fontname, fontsize,
    showtime.


# ttips.Create(widget, text, bgcol, fgcol, fontname, fontsize, showtime)

Note: Pycodestyle is ok wit tis code apart from the unamed exception,
Pylint thinks its trash code almost, rated 3.1\10. As it's not my
code I am not fixing all the PEP8 for now, done a lot of it though.
stevepython.wordpress.com
"""
#====================================================================================
#Professora esse, programa eu consegui pega pela internet, para adicionar comentario
#====================================================================================
import tkinter as tk


class Create(object):
    """Create a tooltip for a given widget."""
    def __init__(self, widget,
                 text='widget info',
                 bgcol='yellow',
                 fgcol='black',
                 fontname='times',
                 fontsize=16,
                 showtime=10):

        self.widget = widget
        self.text = text
        self.bgcol = bgcol
        self.fgcol = fgcol
        self.fontname = fontname
        self.fontsize = fontsize
        self.showtime = showtime

        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox('insert')
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        # Creates a toplevel window.
        self.tw = tk.Toplevel(self.widget)

        # Leaves only the label and removes the app window.
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry('+%d+%d' % (x, y))

        label = tk.Label(self.tw,
                         text=self.text,
                         justify='left',
                         bg=self.bgcol,
                         fg=self.fgcol,
                         relief='solid',
                         borderwidth=1,
                         font=(self.fontname, self.fontsize, "normal"))
        label.pack(ipadx=1)

        # Close tooltip after showtime delay.
        label.after(self.showtime * 1000, self.close)

    def close(self, event=None):
        try:
            if self.tw:
                self.tw.destroy()
        except:
            pass
