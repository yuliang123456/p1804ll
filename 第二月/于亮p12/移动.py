import pygame
def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片，获取倒 代码中
    background = pygame.image.load('./images/background.png')
    bad = pygame.image.load('./images/hero1.png')
    #把图片加载倒游戏窗口上
    #screen.blit(background,(0,0))
    rect = pygame.Rect((400-100)/2,350,300,224)

    clock=pygame.time.Clock()#获得游戏时钟 控制器
    #刷新显示
    #pygame.display.update()
    #防止一闪而退
    move_step=30
    while True:
        screen.blit(background,(0,0))
        screen.blit(bad,rect)
        #刷新显示
        #rect.x += 1
        #if rect.x >400:
         #   rect.x =400
        #游戏事件的监听
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:#退出游戏
                print('游戏退出')
                pygame.quit()
                exit()#退出程序
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect.y -= move_step
                elif event.key == pygame.K_DOWN:

                    rect.y += move_step
                elif event.key == pygame.K_LEFT:
                    rect.x -= move_step
                elif event.key == pygame.K_RIGHT:
                    rect.x += move_step
            elif event.type == pygame.KEYUP:
                pass
        pygame.display.update()
        clock.tick(60)
'''
feiji = pygame.Rect(100,500,50,50)
print('x=',feiji.x)
print('y=',feiji.y)
print('width=',feiji.width)
print('height=',feiji.height)
'''
if __name__== '__main__':
    main()
