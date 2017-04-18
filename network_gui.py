import gi
import subprocess
import time

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Network Sniffer")
        self.set_default_size(480, 320)
        self.set_border_width(10)
        grid = Gtk.Grid()
        self.add(grid)

        #Label met tekst
        label = Gtk.Label()
        label.set_label("Hoelang moet de scan duren: ")
        grid.add(label)

        #Button voor 5 seconden
        button = Gtk.Button.new_with_label("5 Seconden")
        button.connect("clicked", self.vijf_seconden)
        grid.attach(button, 1, 0, 1, 1)

        # Button voor 30 seconden
        button = Gtk.Button.new_with_label("30 Seconden")
        button.connect("clicked", self.dertig_seconden)
        grid.attach(button, 1, 1, 1, 1)

        # Button voor 1 Minuut
        button = Gtk.Button.new_with_mnemonic("1 Minuut")
        button.connect("clicked", self.een_minuut)
        grid.attach(button, 1, 2, 1, 1)

        # Button voor 15 minuten
        button = Gtk.Button.new_with_mnemonic("15 Minuten")
        button.connect("clicked", self.vijftien_minuten)
        grid.attach(button, 1, 3, 1, 1)

        # Button voor 15 minuten
        button = Gtk.Button.new_with_mnemonic("Sluiten")
        button.connect("clicked", self.on_close_clicked)
        grid.attach(button, 1, 4, 1, 1)


    def vijf_seconden(self, button):
        process = subprocess.Popen(['python3', 'Network.py'])
        time.sleep(5)
        process.terminate()
        subprocess.Popen(['python3', 'network_read.py'])
        print("Network Sniffing is gestopt")

    def dertig_seconden(self, button):
        process = subprocess.Popen(['python3', 'Network.py'])
        time.sleep(30)
        process.terminate()
        subprocess.Popen(['python3', 'network_read.py'])
        print("Network Sniffing is gestopt")

    def een_minuut(self, button):
        process = subprocess.Popen(['python3', 'Network.py'])
        time.sleep(60)
        process.terminate()
        subprocess.Popen(['python3', 'network_read.py'])
        print("Network Sniffing is gestopt")

    def vijftien_minuten(self, button):
        process = subprocess.Popen(['python3', 'Network.py'])
        time.sleep(900)
        process.terminate()
        subprocess.Popen(['python3', 'network_read.py'])
        print("Network Sniffing is gestopt")

    def on_close_clicked(self, button):
        print("Network Sniffing wordt afgesloten")
        Gtk.main_quit()

win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()