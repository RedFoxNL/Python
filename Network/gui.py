import gi
import subprocess
import time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Raspberry Pi Control Centre")
        self.set_default_size(480, 320)
        grid = Gtk.Grid()
        self.add(grid)

        #Label met tekst
        label = Gtk.Label()
        label.set_label("Kies een optie: ")
        grid.add(label)

        #button
        self.button = Gtk.Button(label="Netwerk Monitor ")
        self.button.connect("clicked", self.second_window)
        grid.attach(self.button, 1, 0, 1, 1)


    def second_window(self, widget):
        subprocess.Popen(['python3', 'network_gui.py'])


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
