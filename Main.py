from graphics import *

def main():
    win = GraphWin("Super Python RPG", 800, 600)
    rect = Rectangle(Point(10,10), Point(100,100))
    rect.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()