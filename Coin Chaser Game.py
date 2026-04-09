

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Chaser")

player_size = 50
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

coin_size = 20
coin_x = random.randint(0, screen_width - coin_size)
coin_y = random.randint(0, screen_height - coin_size)

score = 0
font = pygame.font.SysFont("Arial", 32)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
        player_y += player_speed

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_x = random.randint(0, screen_width - coin_size)
        coin_y = random.randint(0, screen_height - coin_size)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    pygame.draw.rect(screen, (255, 255, 0), coin_rect)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
