import curses
import papermud
import zmq
import os

context = zmq.Context()
socket = context.socket(zmq.REQ)  # pylint: disable=no-member

if "MUDSERVER" in os.environ.keys():
    socket.connect("tcp://" + os.environ["MUDSERVER"] + ":5555")
else:
    socket.connect("tcp://paperserver:5555")

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(True)

win = curses.newwin(20, 40, 0, 10)

curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)


lal = papermud.rendermenu(
    0, 2, win, ["this", "is", "a", "test", "lol", "going", "good", "so", "far"])

socket.send_pyobj(lal)
response = socket.recv_pyobj()

stdscr.clear()
stdscr.refresh()

lal2 = papermud.rendermenu(
    0, 2, stdscr, response)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

print("lal", lal)
print("response", response)
