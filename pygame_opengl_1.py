# Os pacotes do propio Python.
import sys;

# Importamos o pygame.
import pygame;

# Importamos GL como GL11.
from OpenGL import GL as GL11, GLU;

# util e uma package com varias utilidades que vai nos ajudar duraten o desenvolvimento.
from util import util;

# Variaveis que vamos usar.
width, height = 800, 600;         # Tamanho da janela.
background    = [150, 150, 150];  # Cor do background do conteudo da janela.
partialTicks  = 0;                # Tempo parcial para calcular delta e lerp.
fps           = 75;               # FPS locker do pygame.

# Iniciamos o pygame.
pygame.init();

# Principal variavel do pygame para o display.     Dois buffers       OpenGL.
display = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL);

# Aqui setamos o titulo.
pygame.display.set_caption("Fisica com o Rina! - ep 1");

# Relogio do pygame para mexer com delta time e partial ticks.
clock = pygame.time.Clock();

# Inicializamos o OpenGL.
# Como isso nao e uma aplicacao 3D, nao precisamos investir aqui em matrix.
GLU.gluOrtho2D(0, width, height, 0); # Direcionamos os valores widht e height no ortho2D para sincronizar o tamanho com as coisas desenhadas.

# Rectangulos usados no exemplo.
rectTest  = util.Rect(0, 0, 20, 20);
rectTest2 = util.Rect(width / 2 - 20, height / 2 - 20, 20, 20);

while True:
	# Setamos o clock e dividimos pelo fps, resultando em um partil ticks.
	partialTicks = clock.tick(fps) / fps;

	# Obtemos a lista dos eventos presentes.
	eventList = pygame.event.get();

	# Listamos em um for e verificamos.
	for event in eventList:
		if event.type == pygame.QUIT: # caso voce apertar fechar na janela.
			# ela nao vem por padrao esse fechar, entao temos que fazer codificalmente.
			pygame.quit();

			# Usamos a package do Python sys (sistema) para parar a execucao do Python.
			sys.exit();

	# Limpamos os buffers color e depth buffer, depois colorimos a tela.
	GL11.glClear(GL11.GL_COLOR_BUFFER_BIT | GL11.GL_DEPTH_BUFFER_BIT);
	GL11.glClearColor(background[0] / 255.0, background[1] / 255.0, background[2] / 255.0, 0);

	# Renderizamos o rect.
	util.color((255 - util.distance2r(rectTest, rectTest2)), 0, 0, 255);
	util.drawRect(rectTest);

	util.color(255, 255, 255, 255);
	util.drawRect(rectTest2);

	# Obtemos a posiacao do mouse pelo pygame.
	mousePosition = pygame.mouse.get_pos();

	# Interpolarizemos a posicao do mouse e setamos para valores de x, y do rectTest.
	rectTest.x = util.lerp(rectTest.x, mousePosition[0] - rectTest.w / 2, partialTicks);
	rectTest.y = util.lerp(rectTest.y, mousePosition[1] - rectTest.h / 2, partialTicks);

	# Loop.
	pygame.display.flip();