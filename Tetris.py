import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
#Inicijalizujemo grid tako sto u pocetku postavljamo globalne varijable
pygame.font.init()
#POstavljamo varijble screen width i height, takodje i play height
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30


top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


#ovo nam je klasa za kockice,ima 3 argumenta za inicijalizaciju,x y i shape
class Piece(object):
    def __init__(self,x,y,shape):
        self.x=x
        self.y=y
        self.shape=shape
        self.color=shape_colors[shapes.index(shape)]
        self.rotation=0

#Metoda za pravljenje grida
def create_grid(locked_positions={}):

    grid=[[(0,0,0) for x in range(10)] for x in range(20)]
    #Pravimo matricu koja je 20*10 tj ima 20 nizova od po 10 clanova
    #ili ti pravimo matricu sa 20 kolona i 10 redova

    #Idemo kroz matricu sa 2 for petlje
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(j,i) in locked_positions:#ako je set od (i,j) u locked_positions
                c=locked_positions[(j,i)]#C dovija vrijednost neke boje
                grid[i][j]=c        #popunjavamo grid tom bojom
    return grid


def convert_shape_format(shape):
    positions=[]
    format=shape.shape[shape.rotation % len(shape.shape)]

    for i,line in enumerate(format):
        row= list(line)
        for j,column in enumerate(row):
            if column == '0':
                positions.append((shape.x+j,shape.y+i))

    for i,pos in enumerate(positions):
        positions[i] =(pos [0]-2,pos[1]-4)

def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def get_shape(shapes):
    return Piece(5,0,random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, grid):
    sx=top_left_x
    sy=top_left_y

    for i in range(len(grid)):
        pygame.draw(surface,(128,128,128),(sx,sy+i*block_size), (sx+play_width,sy+i*block_size))
        for j in range(len(grid[i])):
            pygame.draw(surface,(128,128,128),(sx+j*block_size,sy), (sx+j*block_size,sy+play_height))

def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def draw_window(surface,grid):
    surface.fill((0,0,0))

    pygame.font.init()
    font=pygame.font.SysFont('comicsans',60)
    label=font.render('Teris',1,(255,255,255))

    surface.blit(label,(top_left_x+ play_width/2-(label.get_width()/2),30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface,grid[i][j],(top_left_x+ j*block_size,top_left_y+ i*block_size,block_size,block_size),0)

    pygame.draw.rect(surface,(255,0,0),(top_left_x,top_left_y,play_width,play_height),4)


    draw_grid(surface,grid)
    pygame.display.update()


def main(win):

    locked_positions={}
    grid=create_grid(locked_positions)

    change_piece=False
    run=True
    current_piece=get_shape()
    clock=pygame.time.Clock()
    fall_time=0

    while run:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                run=False
                break
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece,grid)):
                        current_piece +=1
                if e.key == pygame.K_RIGHT:
                    current_piece +=1
                    if not (valid_space(current_piece,grid)):
                        current_piece -=1
                if e.key == pygame.K_DOWN:
                    current_piece +=1
                    if not (valid_space(current_piece,grid)):
                        current_piece -=1
                if e.key == pygame.K_UP:
                    current_piece.rotation +=1
                    if not (valid_space(current_piece,grid)):
                        current_piece -=1

        draw_window(win,grid)

def main_menu():
    pass


win=pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption('Tetrs')
main_menu()  # start game

