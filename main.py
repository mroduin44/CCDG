HEIGHT = 730
WIDTH = 1366

alien = Actor('alien')
alien.right = 0, 365 

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
    
def on_mouse_down():
    print("Mouse button clicked")

def on_mouse_down(pos):
    print("Mouse button clicked at", pos)

def on_mouse_down(button):
    print("Mouse button", button, "clicked")

def on_mouse_down(pos, button):
    print("Mouse button", button, "clicked at", pos)
