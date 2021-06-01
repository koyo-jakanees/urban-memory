import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ExampleWindow(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="hello GTk world!")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("hello Gtk World")


def main():
    win = ExampleWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()