#My final Project
import pygame
import sys


def main():
    
    pygame.init()
    pygame.display.set_caption('Silly SFX')
    txtFont= pygame.font.SysFont('cambria',18)
    resolution =((500,500))
    bg_color = pygame.Color(54,24,56)
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
                button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(95,95))
                button_txt = txtFont.render(self.text, True,'dark gray')
            else:
                button_txt = txtFont.render(self.text, True, 'black')
                button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(100,100))
            
            
            pygame.draw.rect(screen ,self.color, button_rect, 0,5)
            screen.blit(button_txt, (self.x_pos +3, self.y_pos +20))

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]
            button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(100,100))
            if click and button_rect.collidepoint(mouse_pos) and self.enabled:
                return True
            else:
                return False

    channel = pygame.mixer.Channel(0)
    #This is where you choose the sound effect files to place per button(mp3,wav,aiff)
    sfx1 = pygame.mixer.Sound('Flapjack_Scream.mp3')
    sfx2 = pygame.mixer.Sound('Vine_Boom.mp3')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(bg_color)
        button01 = Button('Scream', 70,50,(227,68,86),True)
        button02 = Button('Thud', 190,50,(122,213,104),True)
        button03 = Button('sfx3',310,50,'yellow',True)
        
        #Code for the sounds to play
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button01.check_click():
                channel.play(sfx1)
            if button02.check_click():
                channel.play(sfx2)

        #Code for the Keyboard Shortcuts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            channel.play(sfx1)

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()