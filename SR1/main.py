from gl import Renderer, _color_

#################################

width = 1024
height = 512
white = _color_(1, 1, 1)
black = _color_(0, 0, 0)

rend = Renderer(width, height)

#################################

rend.glCreateWindow(width, height)

rend.glViewPort(int(width/4), int(height/4), int(width/2), int(height/2))

rend.glClearColor(0, 0, 0)
rend.glClear()
rend.glClearViewPort(black)

#################################

rend.glVertex(-1, -1)
rend.glVertex(0, 0)
rend.glVertex(1, 1)

#################################

rend.write("SR1.bmp")
