#My final Project
import pygame
import sys





def main():
    
    pygame.init()
    pygame.display.set_caption('Silly SFX')
    txtFont= pygame.font.SysFont('cambria',18)
    resolution =((500,500))
    bg_color = pygame.Color(255,255,255)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    
    #Button Object
    class Button:
        def __init__(self,text,x_pos,y_pos,enabled):
            self.text =text
            self.x_pos =x_pos
            self.y_pos =y_pos
            self.enabled = enabled
            self.draw()

        def draw(self):
            button_txt = txtFont.render(self.text, True, 'black')
            button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(70,70))
            pygame.draw.rect(screen , 'red', button_rect, 0,5)
            screen.blit(button_txt, (self.x_pos +3, self.y_pos +20))



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(bg_color)
        my_button = Button('Silly fart', 10,10, True)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()