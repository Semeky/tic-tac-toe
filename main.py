import pygame

pygame.init()
fps = 30
cell_size = 100
otp = 4
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cell_size * 3 + otp * 4, cell_size * 3 + otp * 4))
mas = [[0]*3 for i in range(3)]
print(mas)
query = 0 
while True:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            x_col = x_mouse // (cell_size+otp)
            y_col = y_mouse // (cell_size+otp)
            mas[row][col] = 'x'
            if query%2==0:
                
    for row in range(3):
        for col in range(3):
            x = col*cell_size + (col+1)*otp
            y = row*cell_size + (row+1)*otp
            pygame.draw.rect(screen, pygame.Color('White'), (x,y,cell_size,cell_size))
    # pygame.draw.line(screen, (pygame.Color('black')), [0, res / 3], [res, res/ 3], 3)
    # pygame.draw.line(screen, (pygame.Color('black')), [0, res-(res / 3)], [res, res-(res/ 3)], 3)
    # pygame.draw.line(screen, (pygame.Color('black')), [res / 3, 0], [res/ 3, res], 3)
    # pygame.draw.line(screen, (pygame.Color('black')), [res-(res / 3), 0], [res-(res/ 3), res], 3)
    pygame.display.flip()
    clock.tick(fps)