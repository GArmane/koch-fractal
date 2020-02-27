from TurtleWorld import *


TURTLE_X = -150
TURTLE_Y = 100
TURTLE_DELAY = 0.01
KOCH_LENGHT = 300


def drawSnowFlake(turtle, lenght):
	"""
	Desenha um floco de Koch fazendo chamadas a função
	drawKoch.
	"""
	for _ in range(3):
		drawKoch(turtle, lenght)
		rt(turtle, 120)

'''	
def drawStar(turtle, lenght):
	"""
	Usa um objeto turtle do tipo Turtle e desenha
	um estrela de Koch com comprimento lenght, passando
	parâmetros para função drawKoch.
	"""
	for _ in range(3):
		drawKoch(turtle, lenght)
		rt(turtle, 120)
'''

def drawKoch(turtle, lenght):
	"""
	Recursiva, tem como entradas um objeto do tipo Turtle
	e um comprimento lenght. Acha o menor comprimento de linha
	possível para qualquer segmento e desenha esta linha
	chamando a próprio função completando o algorítmo de Koch.
	"""
	if lenght < 3:
		fd(turtle, lenght)
		return
	else:
		angle = 60
		div_lenght = lenght / 3
		drawKoch(turtle, div_lenght)
		lt(turtle, angle)
		drawKoch(turtle, div_lenght)
		rt(turtle, angle * 2)
		drawKoch(turtle, div_lenght)
		lt(turtle, angle)
		drawKoch(turtle, div_lenght)

if __name__ == '__main__':
	"""
	Método principal, executado caso nao tenha sido importado
	Cria um mundo TurtleWorld, um objeto Turtle, redesenha-o em
	uma posição turtle_x e turtle_y com delay de desenho 
	draw_delay.
		Faz chamada a função koch para desenho de uma curva de
	Koch, usando objeto Turtle e comprimento koch_lenght
	"""
	world = TurtleWorld()
	turtle = Turtle()
	turtle.x = TURTLE_X
	turtle.y = TURTLE_Y
	turtle.delay = TURTLE_DELAY
	turtle.redraw()

	drawSnowFlake(turtle, KOCH_LENGHT)

	wait_for_user()
