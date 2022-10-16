# SR1
# Mario de Leon 19019
# Graficos por computadora basado en lo escrito por Ing. Carlos Alonso / Ing. Dennis Aldana

import struct


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2 bytes
    return struct.pack('=h', w)


def dword(d):
    # 4 bytes
    return struct.pack('=l', d)


def _color_(r, g, b):
    return bytes([int(b*255),
                  int(g*255),
                  int(r*255)])


class Renderer(object):
    def __init__(init, width, height):
        init.width = width
        init.height = height
        init.clearColor = _color_(0, 0, 0)
        init.currColor = _color_(1, 1, 1)
        init.glViewPort(0, 0, init.width, init.height)
        init.glClear()

    # El area donde se va a dibujar
    def glCreateWindow(init, width, height):
        init.width = width
        init.height = height
        init.glClear()

    # Utiliza las coordenadas
    def glViewPort(init, x, y, width, height):
        init.viewportX = x
        init.viewportY = y
        init.viewportWidth = width
        init.viewportHeight = height

    # Limpia los pixeles de la pantalla poniendolos en blanco o negro
    def glClear(init):
        init.framebuffer = [[init.clearColor for y in range(
            init.height)]for x in range(init.width)]

    # Coloca color de fondo
    def glClearColor(init, r, g, b):
        init.clearColor = _color_(r, g, b)

    # Dibuja un punto
    def glVertex(init, vertexX, vertexY, color=None):
        x = int((vertexX+1)*(init.viewportWidth/2)+init.viewportX)
        y = int((vertexY+1)*(init.viewportHeight/2)+init.viewportY)

        if (0 <= x < init.width) and (0 <= y < init.height):
            init.framebuffer[x][y] = color or init.currColor

    # Se establece el color de dibujo, si no tiene nada se dibuja blanco
    def glColor(init, r, g, b):
        init.currColor = _color_(r, g, b)

    def glClearViewPort(init, color=None):
        for x in range(init.viewportX, init.viewportX + init.viewportWidth):
            for y in range(init.viewportY, init.viewportY + init.viewportHeight):
                init.glVertex(x, y, color)

    # Crea un archivo BMP
    def write(init, filename):
        with open(filename, "bw") as file:
            # pixel header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + init.width * init.height * 3))
            file.write(word(0))
            file.write(word(0))
            file.write(dword(14 + 40))

            # informacion del header
            file.write(dword(40))
            file.write(dword(init.width))
            file.write(dword(init.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(init.width * init.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # pixel data
            for y in range(init.height):
                for x in range(init.width):
                    file.write(init.framebuffer[x][y])
