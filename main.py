import pygame

def check_win(mas,sign):
    zeroes = 0
    for row in mas:
        zeroes+=row.count(0)
        if row.count(sign)== 3:
            return sign
    for col in range(3):
        if mas[0][col]==sign and mas[1][col]==sign and mas[2][col]==sign:
            return sign
    if mas[0][0]==sign and mas[1][1]==sign and mas[2][2]==sign:
        return sign
    if mas[0][2]==sign and mas[1][1]==sign and mas[2][0]==sign:
        return sign
    if zeroes == 0:
        return 'Piece'
    return False
    
pygame.init()
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
fps = 30
cell_size = 100
otp = 10
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cell_size * 3 + otp * 4, cell_size * 3 + otp * 4))
mas = [[0]*3 for i in range(3)]
query = 0
game_over = False
while True:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (cell_size+otp)
            row = y_mouse // (cell_size+otp)
            if mas[row][col] == 0:       
                if query%2==0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query+=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            query = 0
            screen.fill(black)

    if not game_over: 
        for row in range(3):
            for col in range(3):
                if mas[row][col]=='x':
                    color = red
                elif mas[row][col]=='o':
                    color = green
                else:
                    color = white
                x = col*cell_size + (col+1)*otp
                y = row*cell_size + (row+1)*otp
                pygame.draw.rect(screen, color, (x,y,cell_size,cell_size))
    if (query-1)%2==0:
        game_over = check_win(mas,'x')
    else:
        game_over = check_win(mas, 'o')
    
    if game_over:
        print('game over')
    pygame.display.flip()
    clock.tick(fps)