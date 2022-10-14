import sys,pygame
import model
from math import log2

#Dimension de la fenetre
size = width, height = 480,500
#Dimension du cadre de jeu
playRegion = 480,480
FPS = 60

#Couleur
black = (0,0,0)
white = (255,255,255)
fontColor = (82,52,42)
defaultTileColor = (232,232,232)
titleBoarderColor = fontColor

#Desing du jeu
boardSize = 4
def drawBoard(screen, board) :
    screen.fill(black)
    for i in range(board.boardSize):
        for j in range(board.boardSize):
            color = defaultTileColor
            numberText = ''
            if board.board[i][j] != 0 :
                gComponent = 235 - log2(board.board[i][j])*((235-52)/(board.boardSize**2))
                color = (235, gComponent, 52)
                numberText = str(board.board[i][j])
            rect = pygame.Rect(j*playRegion[0]/board.boardSize,
                                i*playRegion[1]/board.boardSize,
                                playRegion[0]/board.boardSize,
                                playRegion[1]/board.boardSize)
            
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, fontColor, rect, 1)
            
            fontImage = tileFont.render(numberText, 0,fontColor)
            if fontImage.get_width() > playRegion[0]/board.boardSize :
                fontImage = pygame.transform.scale(fontImage,
                                                   (playRegion[0]/boardSize,
                                                    fontImage.get_height()/fontImage.get_width()*playRegion[0]/board.boardSize))
            screen.blit(fontImage,
                        (j*playRegion[0]/board.boardSize + (playRegion[0]/board.boardSize - fontImage.get_width())/2,
                         i*playRegion[1]/board.boardSize + (playRegion[1]/board.boardSize - fontImage.get_height())/2))
    fontImage = scoreFont.render("Scrore : {:,}".format(board.score), 1, white)
    screen.blit(fontImage, (1, playRegion[1]+1))

def handleInput(event, board) :
    if event.type == pygame.QUIT : sys.exit()
    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_RIGHT :
            board.move(model.RIGHT)   
        elif event.key == pygame.K_LEFT :
            board.move(model.LEFT)  
        elif event.key == pygame.K_UP :
            board.move(model.UP)         
        elif event.key == pygame.K_DOWN :
            board.move(model.DOWN) 
        elif event.key == pygame.K_ESCAPE :
            sys.exit()
            
    return board  

def gameLoop() :
    clock = pygame.time.Clock()
    board = model.Board(boardSize)
    
    while 1:
        for event in pygame.event.get() :
            board = handleInput(event,board)
        
        drawBoard(screen,board)
        pygame.display.flip()
        clock.tick(FPS)
        
            
    

if __name__ == '__main__':
    global screen 
    global tileFont
    global scoreFont
    global pool
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048")
    tileFont = pygame.font.SysFont("", 72)
    scoreFont = pygame.font.SysFont("", 22)
    gameLoop()