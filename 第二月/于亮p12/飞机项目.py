import pygame
import time
from random import randint
class Plane(object):
    def __init__(self,screen,images,x,y):
        self.screen = screen
        self.images = images
        self.x = x
        self.y = y
        self.w = 0
        self.h = 0
        self.load_image = pygame.image.load(self.images)
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.fire_list = []
        self.bom = []  # 我机的爆炸
        self.enemy_bom = []  # 敌机的爆炸
        self.num = 0
        self.create_bomb()
    def display(self):
        self.screen.blit(self.load_image,self.rect)
        for i in self.fire_list:
            if i.judge():
                self.fire_list.remove(i)
            i.display()
            i.move(3)
    def create_bomb(self):
        self.bom.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.bom.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.bom.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.bom.append(pygame.image.load('./images/hero_blowup_n4.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down1.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down2.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down3.png'))
        self.enemy_bom.append(pygame.image.load('./images/enemy0_down4.png'))
class Hero_plane(Plane):
    def __init__(self,screen,images):
        super().__init__(screen,images,330,670)
        self.fire_list = []
        self.num = -2
    def fire(self):
        self.fire_list.append(Hero_bullet(self.screen,'./images/bullet-3.gif',self.rect.x,self.rect.y))
    def bomb(self):
        a = 0
        for i in self.bom:
            self.screen.blit(i,(self.rect.x,self.rect.y))
            pygame.display.update()
            time.sleep(0.4)
            if a == 3:
                exit()
            a += 1
class Enemy_plane(Plane):
    ''' 里面有一个Boss机 的方法'''
    def __init__(self,screen,images):
        super().__init__(screen,images,randint(0,390),randint(1,200))
        self.flag = 'right'
        self.num = 2
        self.hit = False
    def move(self):
        if self.flag == 'right':
            self.rect.x += 3
            self.rect.y += 1
        else:
            self.rect.x -= 2
            self.rect.y += 1
        if self.rect.x >= 398:
            self.flag = 'left'
        elif self.rect.x <= 0:
            self.flag = 'right'
    def fire(self):
        self.fire_list.append(Enemy_bullet(self.screen,'./images/bullet-1.gif',self.rect.x,self.rect.y))
    def bomb(self):
        for ss in self.enemy_bom:
            self.screen.blit(ss,(self.rect.x,self.rect.y))
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(20)
        self.hit = True

# 定义敌机群类
class Power(object):
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images
        self.power_list = []  #   存放 敌机的列表
    def add(self):
        self.power_list.append(Enemy_plane(self.screen,self.images))
    def display(self,hero_plane):
        for i in self.power_list:
            i.display()
            i.move()
            if randint(1,110) == 6:
                i.fire()
            if i.rect.y > 800:
                self.power_list.remove(i)
            jiluo(hero_plane,i,51,39)
            jiluo(i,hero_plane,100,124)
            if i.hit == True:
                self.power_list.remove(i)

def jiluo(zidan,zhui,w,h):
    for i in zidan.fire_list:
        if (zhui.rect.x < i.x < zhui.rect.x +w) and (zhui.rect.y < i.y < zhui.rect.y + h):
            zhui.bomb()
class Bullet(object):
    def __init__(self,screen,images,x,y):
        self.images = images
        self.load_images = pygame.image.load(self.images)
        self.x = x
        self.y = y
    def display(self):
        self.screen.blit(self.load_images,(self.x,self.y))
    def judge(self):
        if (self.y > 800) or (self.y <0):
            return True
        else:
            return False
class Hero_bullet(Bullet):
    def __init__(self,screen,images,x,y):
        super().__init__(screen,images,x,y)
        self.screen = screen
        self.images = images
        self.x = x
        self.y = y
    def move(self,num):
        self.y -= num
class Enemy_bullet(Bullet):
    def __init__(self,screen,images,x,y):
        super().__init__(screen,images,x,y)
        self.screen = screen
        self.images = images
        self.x = x
        self.y = y
    def move(self,num):
        self.y += num

time_clock = pygame.USEREVENT
pygame.time.set_timer(time_clock,1500)
def key_control(hero,move_step,power,enemy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('游戏退出')
            pygame.quit()
            exit()
        if event.type == time_clock:
            power.add()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y >= 5:
            hero.rect.y -= move_step
    elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y <= 676:
            hero.rect.y += move_step
    elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x >= 0:
            hero.rect.x -= move_step
    elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x <= 350:
            hero.rect.x += move_step
    elif keys_pressed[pygame.K_b]:
        print(hero.hit)
        enemy.bomb()
def main():
    screen = pygame.display.set_mode((450,800),0,32)
    background = pygame.image.load('./images/background.png')

    hero_plane = Hero_plane(screen,'./images/hero.gif')

    enemy_plane = Enemy_plane(screen,'./images/enemy-1.gif')

    power = Power(screen,'./images/enemy-1.gif')
    power.add()

    while True:
        screen.blit(background,(0,0))
        hero_plane.display()
        power.display(hero_plane)

        key_control(hero_plane,3,power,enemy_plane)
        pygame.display.update()
if __name__ == '__main__':
    main()


