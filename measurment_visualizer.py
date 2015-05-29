import pygame, sys

from math import pi

from linda.Vec2D import Vec2D
from linda.Circle import Circle
from linda.LineSegment import LineSegment
from linda.RobotState import RobotState
from linda.LidarSimulator import LidarSimulator

PX_PER_METER = 300
WIDTH = int(3.0 * PX_PER_METER)
HEIGHT = int(2.0 * PX_PER_METER)
 
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)

BOTTOM_WALL = LineSegment(Vec2D(0.0, 0.0), Vec2D(3.0, 0.0))
RIGHT_WALL = LineSegment(Vec2D(3.0, 0.0), Vec2D(3.0, 2.0))
TOP_WALL = LineSegment(Vec2D(3.0, 2.0), Vec2D(0.0, 2.0))
LEFT_WALL = LineSegment(Vec2D(0.0, 2.0), Vec2D(0.0, 0.0))

WALLS = [BOTTOM_WALL, RIGHT_WALL, TOP_WALL, LEFT_WALL]

SPEED = 0.1
OMEGA = pi

def main():

    robot_state = RobotState(1.0, 1.0, 0.0)

    forward = False
    backward = False
    left = False
    right = False

    clk = pygame.time.Clock()

    circles = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    forward = True
                elif event.key == pygame.K_s:
                    backward = True
                elif event.key == pygame.K_a:
                    left = True
                elif event.key == pygame.K_d:
                    right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    forward = False
                elif event.key == pygame.K_s:
                    backward = False
                elif event.key == pygame.K_a:
                    left = False
                elif event.key == pygame.K_d:
                    right = False

        SCREEN.fill(BLACK)

        delta_t = clk.tick(10) / 1000

        if forward:
            robot_state = advance_robot(robot_state, SPEED * delta_t)
        if backward:
            robot_state = advance_robot(robot_state, -SPEED * delta_t)
        if left:
            robot_state = rotate_robot(robot_state, OMEGA * delta_t)
        if right:
            robot_state = rotate_robot(robot_state, -OMEGA * delta_t)

        draw_env(WALLS, circles)

        draw_robot(robot_state)
        
        pygame.display.update()

def advance_robot(robot_state, amnt):
    pos = Vec2D(robot_state.x, robot_state.y)
    direction = Vec2D(1, 0).rotate(robot_state.theta)

    n_pos = pos + direction * amnt

    return RobotState(n_pos.pos_x, n_pos.pos_y, robot_state.theta)

def rotate_robot(robot_state, amnt):
    return RobotState(robot_state.x, robot_state.y, robot_state.theta + amnt)

def world_to_screen(p):
    return (int(p.pos_x * PX_PER_METER), HEIGHT - int(p.pos_y * PX_PER_METER))

def draw_env(walls, circles):
    for wall in walls:
        draw_wall(wall)
    for circle in circles:
        draw_circle(circle)

def draw_circle(circle):
    pygame.draw.circle(SCREEN,
                       BLUE,
                       world_to_screen(circle.pos),
                       int(circle.radius * PX_PER_METER),
                       2)

def draw_wall(wall):
    pygame.draw.line(SCREEN,
                     BLUE,
                     world_to_screen(wall.start),
                     world_to_screen(wall.end),
                     5)

def draw_robot(robot_state):
    pos = Vec2D(robot_state.x, robot_state.y)
    theta = robot_state.theta
    pygame.draw.circle(SCREEN,
                       RED,
                       world_to_screen(pos),
                       int(0.1 * PX_PER_METER),
                       2)
    end_point = pos + Vec2D(0.1, 0).rotate(theta)
    pygame.draw.line(SCREEN,
                     RED,
                     world_to_screen(pos),
                     world_to_screen(end_point),
                     2)



if __name__ == "__main__":
    main()
