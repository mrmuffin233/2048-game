import random,sys,pygame
from settings import Settings

pygame.init()
    #调用类进行后续设置
settings=Settings()
    #创建窗口
screen=pygame.display.set_mode(
    (settings.screen_width,settings.screen_height))
grid = []
for i in range(4):
    row = [0, 0, 0, 0]
    grid.append(row)
score=0


def draw_numbers(value,rect):
    text=settings.font.render(str(value),True,settings.text_color)
    text_rect=text.get_rect()
    text_rect.center=rect.center
    screen.blit(text,text_rect)

def get_grid_color(value):
    colors={
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    }
    return colors[value]

def draw_grid():
    for row in range(4):
        for col in range(4):
            x = col * settings.cell_width
            y = row * settings.cell_height
            cell_rect = pygame.Rect(x, y, settings.cell_width, settings.cell_height)
            cell_color=get_grid_color(grid[row][col])
            pygame.draw.rect(screen, cell_color, cell_rect)
            if grid[row][col]!=0:
                draw_numbers(grid[row][col],cell_rect)


def add_number():
    empty_space=[]
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0:
                check_empty=(row,col)
                empty_space.append(check_empty)
    if empty_space:
        chosed_row,chosed_column=random.choice(empty_space)
        grid[chosed_row][chosed_column]=random.choice([2,4])

def move_left():
    global score
    for row in range(4):
        merged=[False]*4
        for col in range(1,4):
            if grid[row][col]!=0:
                c=col
                while c>0 and grid[row][c-1]==0:
                    grid[row][c-1]=grid[row][c]#将非零数字向左移动
                    grid[row][c]=0
                    c-=1
                if c>0 and not merged[c-1] and grid[row][c-1]==grid[row][c]:
                    grid[row][c-1]*=2
                    grid[row][c]=0
                    merged[c-1] = True#c-1对应的列已经被处理过了
                    score+=grid[row][c-1]
 
def move_up():
    global score
    for col in range(4):
        merged = [False] * 4
        for row in range(1, 4):
            if grid[row][col] != 0:
                r = row
                while r > 0 and grid[r - 1][col] == 0:
                    grid[r - 1][col] = grid[r][col]
                    grid[r][col] = 0
                    r -= 1
                if r > 0 and not merged[r - 1] and grid[r - 1][col] == grid[r][col]:
                    grid[r - 1][col] *= 2
                    grid[r][col] = 0
                    merged[r - 1] = True
                    score+=grid[r-1][col]

def move_right():
    global score
    for row in range(4):
        merged=[False]*4
        for col in range(2,-1,-1):#2 1 0
            if grid[row][col]!=0:
                c=col
                while c<3 and grid[row][c+1]==0:
                    grid[row][c+1]=grid[row][c]
                    grid[row][c]=0
                    c+=1
                if c<3 and not merged[c+1] and grid[row][c+1]==grid[row][c]:
                    grid[row][c+1]*=2
                    grid[row][c]=0
                    merged[c+1]=True
                    score+=grid[row][c+1]

def move_down():
    global score
    for col in range(4):
        merged = [False] * 4
        for row in range(2, -1, -1):
            if grid[row][col] != 0:
                r = row
                while r < 3 and grid[r + 1][col] == 0:
                    grid[r + 1][col] = grid[r][col]
                    grid[r][col] = 0
                    r += 1
                if r < 3 and not merged[r + 1] and grid[r + 1][col] == grid[r][col]:
                    grid[r + 1][col] *= 2
                    grid[r][col] = 0
                    merged[r + 1] = True
                    score+=grid[r+1][col]

def check_if_over():#条件是每一格都满，没有可合并的项。认为True是输
    is_full = True  # 假设格子已经满了
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                is_full = False  # 只要有一个格子是空的，那么就不满
            if col < 3 and grid[row][col] == grid[row][col+1]:
                return False  # 可以合并，则游戏未结束
            if row < 3 and grid[row][col] == grid[row+1][col]:
                return False  # 可以合并，则游戏未结束
            if grid[row][col] == 2048:
                win()  # 游戏胜利
                return True
    if is_full:
        lose()  
        return True   # 是满的而且没有可以合并的项，游戏失败
    return False  # 不是满的，则游戏未结束


def lose():
    lose_text=settings.end_font.render('Game Over!',True,(100,100,100))
    lose_text_rect=lose_text.get_rect()
    lose_text_rect.centerx=screen.get_rect().centerx
    lose_text_rect.centery=screen.get_rect().centery-20
    screen.blit(lose_text,lose_text_rect)

def win():
    win_text=settings.end_font.render('You Win!',True,(100,100,100))
    win_text_rect=win_text.get_rect()
    win_text_rect.centerx=screen.get_rect().centerx
    win_text_rect.centery=screen.get_rect().centery-20
    screen.blit(win_text,win_text_rect)

def check_events():
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if not check_if_over():
                if event.key == pygame.K_LEFT:
                    move_left()
                    add_number()
                elif event.key == pygame.K_RIGHT:
                    move_right()
                    add_number()
                elif event.key == pygame.K_UP:
                    move_up()
                    add_number()
                elif event.key == pygame.K_DOWN:
                    move_down()
                    add_number()

def show_score(): 
    score_text = settings.font.render("Score: " + str(score), True, settings.text_color)
    screen.blit(score_text, (10, settings.screen_height -50))#文本矩形的左上角点的坐标
