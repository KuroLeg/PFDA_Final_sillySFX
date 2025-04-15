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
        def __init__(self,text,x_pos,y_pos,color,enabled):
            self.text =text
            self.x_pos =x_pos
            self.y_pos =y_pos
            #self.rect = self.get_rect(center=(self.x_pos,self.y_pos))
            self.color = color
            self.enabled = enabled
            self.draw()

        def draw(self):
            if self.check_click():
                button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(65,65))
                button_txt = txtFont.render(self.text, True,'dark gray')
            else:
                button_txt = txtFont.render(self.text, True, 'black')
                button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(70,70))
            
            
            pygame.draw.rect(screen ,self.color, button_rect, 0,5)
            screen.blit(button_txt, (self.x_pos +3, self.y_pos +20))

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]
            button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(70,70))
            if click and button_rect.collidepoint(mouse_pos) and self.enabled:
                return True
            else:
                return False



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(bg_color)
        my_button = Button('Silly fart', 10,10,(95,200,25),True)
        #print(my_button.check_click())
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()