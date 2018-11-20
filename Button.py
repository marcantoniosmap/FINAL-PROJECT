import pygame.font



class Button():

    def __init__(self, screen, msg,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (242, 234, 234)

        self.text_color = (58,58,58)
        self.font = pygame.font.SysFont("Bahnschrift", 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.x = x
        self.y = y
        self.rect.center = (self.x,self.y)
        self.prep_msg(msg)
        self.sound = pygame.mixer.Sound('click.wav')

    def mouse_hover(self,screen,msg,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 210, 60
        self.button_color = (242, 234, 234)

        self.text_color = (58,58,58)
        self.font = pygame.font.SysFont("Bahnschrift", 22)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.x = x
        self.y = y
        self.rect.center = (self.x,self.y)
        self.prep_msg(msg)
        self.sound = pygame.mixer.Sound('click.wav')


    def mouse_back(self,screen,msg,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (242, 234, 234)

        self.text_color = (58,58,58)
        self.font = pygame.font.SysFont("Bahnschrift", 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.x = x
        self.y = y
        self.rect.center = (self.x,self.y)
        self.prep_msg(msg)
        self.sound = pygame.mixer.Sound('click.wav')

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)

        self.screen.blit(self.msg_image, self.msg_image_rect)

class text1():

    def __init__(self, screen, msg,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 350, 50
        self.button_color = (153, 204, 255)

        self.text_color = (58,58,58)
        self.font = pygame.font.SysFont("Arial", 12)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x,y)
        self.prep_msg(msg)


    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)

        self.screen.blit(self.msg_image, self.msg_image_rect)

class blue_button():

    def __init__(self, screen, msg,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200,50
        self.button_color = (153, 204, 255)

        self.text_color = (15,15,15)
        self.font = pygame.font.SysFont("Bahnschrift", 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x,y)
        self.prep_msg(msg)
        self.sound = pygame.mixer.Sound('click.wav')
    def mouse_hover(self,screen,msg,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 210, 60
        self.button_color = (153, 204, 255)

        self.text_color = (15,15,15)
        self.font = pygame.font.SysFont("Bahnschrift", 22)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.center = (x, y)
        self.prep_msg(msg)
        self.sound = pygame.mixer.Sound('click.wav')


    def mouse_back(self,screen,msg,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200,50
        self.button_color = (153, 204, 255)

        self.text_color = (15,15,15)
        self.font = pygame.font.SysFont("Bahnschrift", 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x,y)
        self.prep_msg(msg)
        self.sound = pygame.mixer.Sound('click.wav')

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)

        self.screen.blit(self.msg_image, self.msg_image_rect)

class Color_button():
    def __init__(self,screen,color,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width=65
        self.height=68
        self.color=color
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = (x,y)
        self.sound = pygame.mixer.Sound('click.wav')


    def draw_button(self):
        self.screen.fill(self.color, self.rect)

class Image_button():
    def __init__(self,screen,image_source,x,y):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width=65
        self.height=68
        self.load=pygame.image.load(image_source)
        self.image=pygame.transform.scale(self.load, (self.width, self.height))

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = (x,y)
        self.sound = pygame.mixer.Sound('click.wav')


    def draw_button(self):
        self.screen.blit(self.image,self.rect)