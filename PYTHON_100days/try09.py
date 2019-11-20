# 使用Pygame进行游戏开发
import pygame 

def main():
    # 初始化pygame
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前的标题
    pygame.display.set_caption('大球吃小球')
    screen.fill((242, 242, 242))
    # 绘制一个圆
    pygame.draw.circle(screen, (255, 0,0), (100, 100), 30, 0)
    # 开启一个时间循环处理发生的事件
    running = True
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
        