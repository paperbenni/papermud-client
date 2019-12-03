#!/usr/bin/env python3
import curses

def rendermenu(y, x, window, items):
    selection = 0
    menuwidth = len(max(items, key=len))
    key = ''
    shortcuts = list("1234567890")
    while True:
        for i in items:
            if items.index(i) == selection:
                window.addstr(y + items.index(i), x, i + " " *
                              (menuwidth - len(i)), curses.color_pair(1))
            else:
                window.addstr(y + items.index(i), x, i + " " *
                              (menuwidth - len(i)), curses.color_pair(2))
        window.refresh()

        key = window.getkey()
        if key == "k":
            if selection <= 0:
                selection = len(items) - 1
            else:
                selection -= 1
        elif key == "j":
            if selection >= len(items) - 1:
                selection = 0
            else:
                selection += 1
        elif key == "g":
            selection = 0
        elif key == "G":
            selection = len(items) - 1
        elif key == " " or key == "\n":
            return items[selection]
        elif key in shortcuts:
            if shortcuts.index(key) < (len(items)):
                selection = shortcuts.index(key)
        elif key == "q":
            break
