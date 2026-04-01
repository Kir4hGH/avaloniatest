#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
import signal

def quit_cb(source):
    Gtk.main_quit()

indicator = AppIndicator3.Indicator.new(
    "test",
    "application-default-icon",
    AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

menu = Gtk.Menu()
item = Gtk.MenuItem(label="Quit")
item.connect("activate", quit_cb)
menu.append(item)
menu.show_all()
indicator.set_menu(menu)

Gtk.main()
