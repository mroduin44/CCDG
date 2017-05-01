HEIGHT = 730
WIDTH = 1366
Position=(0,0)

alien = Actor('alien')
alien.topright = 0, 0 

def draw():
    screen.clear()
    alien.draw()

def update():
    print(Position[0])
    
def on_mouse_down():
    

def on_mouse_down(pos):
    

def on_mouse_down(button):
    

def on_mouse_down(pos, button):
    

def on_mouse_move(pos):
    Position=pos
