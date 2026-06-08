# 2D Asteroids Game (Object-Oriented Programming Practice)

A two-dimensional arcade game built in Python using Pygame. This project was developed as a practical exercise to master foundational software engineering concepts, state tracking loops, and structural Object-Oriented Programming (OOP).

## Core Programming Concepts Applied

* **Object Inheritance:** Used a unified base class to manage shared properties like 2D positions, velocity vectors, and radius scales across distinct game elements (Player, Asteroid, and Shots).
* **Vector Mathematics and Kinematics:** Implemented movement mechanics, velocity adjustments, and angular rotation using standard 2D vector translations.
* **Frame-Rate Decoupling:** Multiplied all physics calculations by delta-time (`dt`) within the main update loop to guarantee identical movement speeds regardless of hardware rendering performance.
* **Collision Matrices:** Programmed basic radial collision checks (`Distance < Radius_A + Radius_B`) to trigger instant state changes like entity splitting, deletion, and game-over conditions.

## Game Mechanics

* **Splitting Behavior:** Large asteroids split into smaller, faster fragments when struck by a projectile vector.
* **Object Lifecycle Management:** Instantiates and removes projectiles from active memory arrays once they cross outside the visual boundaries of the screen.

## Setup and Execution

### 1. Install Pygame

Ensure Python 3 is installed, then pull the required graphics library:

```bash
pip install pygame
```

### 2. Run the Game

Clone the repository and launch the main entry point:

```bash
git clone https://github.com/bharathc10/asteroids.git
cd asteroids
python3 main.py
```

## Controls

* `W/S/A/D` or Arrow Keys to move and rotate.
* `Spacebar` to fire projectiles.
