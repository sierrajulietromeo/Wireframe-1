import pgzrun
import random
import math

# the size of the screen
WIDTH = 800
HEIGHT = 600

# how much a particle slows down by each second
DRAG = 0.8 

# the colour of each particle in R, G, B values
# Now with Original, White, Red, Green and Yellow (you can add more if you want)
COLOURS = []
COLOURS.append((255, 230, 128))
COLOURS.append((255, 255, 255))
COLOURS.append((255, 0, 0))
COLOURS.append((0, 255, 0))
COLOURS.append((0, 0, 255))
COLOURS.append((255, 255, 0))

# the time in seconds for which a particle is displayed
MAX_AGE = 3

# an list to hold the details of the explosion particles on the screen
particles = []

# This function creates a new explosion at the specified screen co-ordinates

def explode(x, y, speed=300, colour = None):

    # these are new particles, so set their age to zero
    age = 0     
    
    # grab a random colour if one isn't specified
    if colour is None:
        colour = random.choice(COLOURS)

    # generate 100 particles per explosion
    for _ in range(100):
    
        # for each particle, generate a random angle and distance
        angle = random.uniform (0, 2 * math.pi)
        radius = random.uniform(0, 1) ** 0.5

        # convert angle and distance from the explosion point into x and y velocity for the particle
        vx = speed * radius * math.sin(angle)
        vy = speed * radius * math.cos(angle)
        
        # add the particle's position, colour, velocity and age to the list
        particles.append((x, y, colour, vx, vy, age))

# This function redraws the screen by plotting each particle in the list

def draw():

    # clear the screen
    screen.clear()
    
    # loop through all the particles in the list
    for x, y, colour, *_ in particles:
        
        # for each particle in the list, plot its position on the screen
        screen.surface.set_at((int(x), int(y)), colour)

# This function updates the list of particles

def update(dt):

    # to update the particle list, create a new empty list
    new_particles = []
    
    # loop through the existing particle list
    for (x, y, colour, vx, vy, age) in particles:
    
        # if a particle was created more than a certain time ago, it can be removed
        if age + dt > MAX_AGE:
            continue
            
        # update the particle's velocity - they slow down over time
        drag = DRAG ** dt
        vx *= drag
        vy *= drag
        
        # update the particle's position according to its velocity
        x += vx * dt
        y += vy * dt
        
        # update the particle's age
        age += dt
        
        # add the particle's new positionm colour, velocity and age to the new list
        new_particles.append((x, y, colour, vx, vy, age))
        
    # replace the current list with the new one
    particles[:] = new_particles

# This function creates an explosion at a random location on the screen

def explode_random():
    # select a random position on the screen
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    
    # call the explosion function for that position (with a little randomness to the speed of the explosion)
    explode(x, y, random.randint(200, 500))

# Randomise the random thingy
random.seed()

# call the random explosion function every 1.5 seconds
clock.schedule_interval(explode_random, 1.5)

pgzrun.go()

