import pymunk
import pygame
import pymunk.pygame_util
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (300, 300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)
    space.add(body, shape)
    shape.elasticity = 1
    return shape

def create_ground(space, width, height):
    ground = [(width/2, height-10), (width, 20)]
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = ground[0]
    shape = pymunk.Poly.create_box(body, ground[1])
    shape.elasticity = 1
    space.add(body, shape)

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    space = pymunk.Space()
    space.gravity = (0, 981)
    ballmass = 20
    ball = create_ball(space, 30, ballmass)
    create_ground(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        massx = ballmass * 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            ball.body.apply_impulse_at_local_point((0, -100), (0, 0))
        if keys[pygame.K_a]:
            ball.body.apply_impulse_at_local_point((-100, 0), (0, 0))
        if keys[pygame.K_s]:
            ball.body.apply_impulse_at_local_point((0, 100), (0, 0))
        if keys[pygame.K_d]:
            ball.body.apply_impulse_at_local_point((100, 0), (0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                ball.mass = massx
                ball.color = (125, 0, 0, 100)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                ball.mass = ballmass
                ball.color = (255, 0, 0, 100)

            
        
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)

