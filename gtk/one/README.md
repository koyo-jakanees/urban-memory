# GTK3 C Programming using Glade

GTK: **GIMP** Toolkit version3 to display a window created using Glade3 user interface designer.
GTK applications are written in C but have several binding in other languages.
Each user interface created by GTK consists of widgets. Implemented in C using GObject, an object-oriented framework for C. Widgets are organized in hierarchy. Window widget in the main container. The user interface is then built by adding buttons, drop-down menus, input fields and other widgets to the window.
It's recommended to use `GtkBuilder` and it's Gtk-specific markup description language. or visual user interface editor like glade.
Why am i going through this?
well as an alternative to popular QT framework but with friendlier licensing and just out of curiosity to expand knowledge on gtk due to it's wide use in the open source world. My first mentor asked why I was using Qt instead of GTK, well the simple answer is, the current developer role that I had involved extending  a qt application and pretty much appeal to some of the popular geospatial tools out there like Arcgis, QGIS, some Autodesk tool under the hood like 3ds Maya thus being in such a domain it makes more sense to delve in Qt.
[ref](https://prognotes.net/2019/10/gtk-programming-introduction/)
[ref](https://developer.gnome.org/gtk4/stable/gtk-getting-started.html)
GTK uses **Glade** as its User interface designer, just like there is a Qt designer.
`sudo apt install glade libgtk-3-dev`
update: GTK4 is now available.
Above command will install required dev tools for gtk
[language Bindings](https://www.gtk.org/docs/language-bindings/index)

to compile the  `main.c` source file

```sh
gcc -o gladewin main.c -Wall `pkg-config --cflags --libs gtk+-3.0` -export-dynamic
```

Note: some python example included to have a feel. If you are comfortable programming in PyQt it shoul be a breeze.

[examples](./examples) contains code to try from the gtk developer main forum for getting started. User Interface is generated programatically instead of using glade visual user interface designer.

```sh
gcc `pkg-config --cflags gtk4` -o example-0 example-0.c `pkg-config --libs gtk4`
```

to run the examples.

## compiling Glib C program using glb

first install the glib dev-tools
`sudo apt install libglib2.0-dev`

compile using:
``gcc main.c `pkg-config --cflags --libs glib-2.0` -o hello`` or `gcc main.c $(pkg-config --cflags --libs glib-2.0) -o hello`

Using pkg-config to display version of  the currently installed GLib
`pkg-config --modversion glib-2.0`

Programmatically check compile the glib_version.c as follows
``gcc glib_version.c `pkg-config --cflags --libs glib-2.0` -o version``
`gcc glib_version.c $(pkg-config --cflags --libs glib-2.0) -o version`