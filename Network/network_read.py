from gi.repository import Gtk

class TextViewWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Netwerk Sniffing Data")

        self.set_default_size(480, 320)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        toolbar = Gtk.Toolbar()
        save_btn = Gtk.ToolButton.new_from_stock(Gtk.STOCK_SAVE)
        save_btn.connect("clicked", self.on_save_clicked)
        toolbar.insert(save_btn, 0)
        quit_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_CANCEL)
        quit_button.connect("clicked", self.quit_button)
        toolbar.insert(quit_button, 1)
        self.box.pack_start(toolbar, False, True, 0)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        scrolledwindow.add(self.textview)
        self.box.pack_start(scrolledwindow, True, True, 0)

        with open('data.txt', 'r') as f:
            data1 = f.read()
            self.textbuffer.set_text(data1)

    def on_save_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Bestand opslaan als", self,
        Gtk.FileChooserAction.SAVE,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            save_file = dialog.get_filename()
            start_iter = self.textbuffer.get_start_iter()
            end_iter = self.textbuffer.get_end_iter()
            text = self.textbuffer.get_text(start_iter, end_iter, True)
            with open(save_file, 'w') as f:
                f.write(text)
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

        dialog.destroy()

    def quit_button(self, widget):
        print("Network Sniffing wordt afgesloten")
        Gtk.main_quit()


win = TextViewWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()