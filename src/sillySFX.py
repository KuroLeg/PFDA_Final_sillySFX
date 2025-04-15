#My final Project
import pygame

def main():
    pygame.init()
    pygame.display.set_caption('Silly SFX')
    resolution =((500,500))
    bg_color = pygame.Color(255,255,255)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(bg_color)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()