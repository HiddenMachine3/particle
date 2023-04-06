import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# todo: move class codes into separate python files and import as modules

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y

    def mult(self, k):
        self.x *= k
        self.y *= k

    def div(self, k):
        self.x /= k
        self.y /= k

    @staticmethod
    def dot2vecs(a, b):
        return Vec2d(a.x * b.x, a.y * b.y)

    @staticmethod
    def add2vecs(a, b):
        return Vec2d(a.x + b.x, a.y + b.y)

    @staticmethod
    def sub2vecs(a, b):
        return Vec2d(a.x - b.x, a.y - b.y)

    def __str__(self):
        return str(self.x) + ", " + str(self.y)


class Particle:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel


particles = []
N = 5
x_bounds = 10
y_bounds = 10

steps = 10

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
marker_size = 50


def init():  # initialising particle positions and velocities
    for i in range(0, N):
        θ = np.random.random() * np.pi * 2  # random angle between 0 and 2 pi

        # initialising with random position within the boundaries
        pos = Vec2d(np.random.random() * x_bounds, np.random.random() * y_bounds)

        # initialising with random velocity with unit speed
        vel = Vec2d(np.cos(θ), np.sin(θ))  # unit vector
        vel.mult(0.1)
        particles.append(Particle(pos, vel))


def update():
    for i in range(0, N):
        # updating positions
        # print("before:", str(particles[i].pos))
        particles[i].pos.add(particles[i].vel)
        # print("after:", str(particles[i].pos))
        # print("supposed to be:", str(Vec2d.add2vecs(particles[i].pos, particles[i].vel)))

        # collision detection
        if particles[i].pos.x >= x_bounds or particles[i].pos.x <= 0:
            particles[i].vel.x *= -1
        if particles[i].pos.y >= y_bounds or particles[i].pos.y <= 0:
            particles[i].vel.y *= -1


def display():
    X, Y = [], []
    for i in range(0, N):
        X.append(particles[i].pos.x)
        Y.append(particles[i].pos.y)

    fig.clear()
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(0, x_bounds), ylim=(0, y_bounds))
    ax.set_xlim(0, x_bounds)
    ax.set_ylim(0, y_bounds)
    s = ax.scatter(X, Y, s=marker_size, cmap="RdBu_r", marker="o",
                   edgecolor='black')


def animate(i):
    update()
    display()


def start():
    init()
    plt.grid(b=None)
    ani = animation.FuncAnimation(fig, animate, interval=100, frames=range(steps))

    ani.save('animation.gif')
    plt.show()


start()
