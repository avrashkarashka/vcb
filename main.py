import pygameimport sys
# Инициализация Pygame
pygame.init()
# Размеры окнаWIDTH = 300
HEIGHT = 300
LINE_WIDTH = 15
CIRCLE_RADIUS = 40
CIRCLE_WIDTH = 15
X_WIDTH = 25
X_HEIGHT = 25
LINE_COLOR = (28, 170, 156)
CIRCLE_COLOR = (242, 85, 96)
X_COLOR = (28, 170, 156)
BG_COLOR = (28, 170, 156)
RED = (242, 85, 96)
WHITE = (255, 255, 255)
LINE_COLOR = (28, 170, 156)
# Создаем окноscreen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
# Игровое полеboard = [[None] * 3 for _ in range(3)]
# Игроки
player = "X"  # X всегда ходит первым
# Функция отрисовки игрового поляdef draw_lines():
    # Горизонтальные линии    pygame.draw.line(screen, LINE_COLOR, (0, 100), (WIDTH, 100), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (0, 200), (WIDTH, 200), LINE_WIDTH)    # Вертикальные линии
pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, HEIGHT), LINE_WIDTH)    
pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, HEIGHT), LINE_WIDTH)
# Функция для отрисовки X и O на экране
def draw_figures():
    for row in range(3):        
        for col in range(3):
            if board[row][col] == "X":                
                pygame.draw.line(screen, X_COLOR, (col * 100 + 15, row * 100 + 15), (col * 100 + 85, row * 100 + 85), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * 100 + 85, row * 100 + 15), (col * 100 + 15, row * 100 + 85), X_WIDTH)            elif board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * 100 + 50, row * 100 + 50), CIRCLE_RADIUS, CIRCLE_WIDTH)
# Функция для проверки победыdef check_winner(player):
    # Проверка по горизонтали    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:            pygame.draw.line(screen, RED, (0, row * 100 + 50), (WIDTH, row * 100 + 50), LINE_WIDTH)
            return True    # Проверка по вертикали
    for col in range(3):        if board[0][col] == board[1][col] == board[2][col] == player:
            pygame.draw.line(screen, RED, (col * 100 + 50, 0), (col * 100 + 50, HEIGHT), LINE_WIDTH)            return True
    # Проверка по диагонали    if board[0][0] == board[1][1] == board[2][2] == player:
        pygame.draw.line(screen, RED, (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)        return True
    if board[0][2] == board[1][1] == board[2][0] == player:        pygame.draw.line(screen, RED, (WIDTH, 0), (0, HEIGHT), LINE_WIDTH)
        return True    return False
# Функция для проверки ничьей
def check_draw():    for row in board:
        for cell in row:            if cell is None:
                return False    return True
# Основной цикл игры
def main():    global player
    game_over = False    screen.fill(BG_COLOR)
    draw_lines()
    while True:        for event in pygame.event.get():
            if event.type == pygame.QUIT:                pygame.quit()
                sys.exit()            if game_over:
                continue            if event.type == pygame.MOUSEBUTTONDOWN:
                # Получаем координаты клика                mouseX = event.pos[0] // 100
                mouseY = event.pos[1] // 100
                # Проверяем, пустая ли клетка                if board[mouseY][mouseX] is None:
                    board[mouseY][mouseX] = player
                    if check_winner(player):                        game_over = True
                    elif check_draw():                        game_over = True
                    player = "O" if player == "X" else "X"  # Меняем игрока
                    draw_figures()
        pygame.display.update()
if name == "__main__":    main()