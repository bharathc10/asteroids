# Object-Oriented Simulation Engine (Vector Mechanics & Kinematics)

A frame-independent, two-dimensional simulation engine engineered in Python using Pygame to model rigid-body mechanics, spatial kinematics, and continuous collision detection. Built as a foundational backend engineering project to develop proficiency in object-oriented programming (OOP), simulation architecture, and deterministic game-loop design.

### ARCHITECTURAL CORE & DESIGN PATTERNS
The project emphasizes software engineering principles rather than simple gameplay scripting.

Classical Mechanics & Vector Mathematics

- Modeled velocity, acceleration, directional movement, and rotational transformations using vector arithmetic.
- Implemented coordinate translation logic for movement across a two-dimensional Cartesian space.
- Applied continuous motion calculations to simulate real-time kinematic behavior.

Object Inheritance & Polymorphism

- Created a shared base entity class responsible for position tracking, movement behavior, and collision boundaries.
- Derived specialized entities such as:
    - Player
    - Projectile
    - Asteroid
- Leveraged inheritance to minimize duplicated logic while enabling entity-specific behavior.

Deterministic State Updates

- Implemented delta-time (dt) propagation throughout the simulation loop.
- Physics calculations remain consistent regardless of rendering frame rate.
- Prevents simulation speed from varying across different hardware configurations.

Spatial Collision Detection

- Used circular collision boundaries for efficient overlap testing.
- Evaluated real-time entity intersections using distance calculations.
- Triggered state transitions including:
    - Asteroid fragmentation
    - Projectile removal
    - Entity destruction
    - Score updates

### SYSTEM CAPABILITIES & LOGIC FLOW
Kinetic Splitting Mechanics

- Large asteroid entities fragment into smaller asteroids when impacted.
- Newly generated fragments inherit modified velocity vectors.
- Creates a cascading destruction and movement system.

Encapsulated Input Processing

- Keyboard events are separated from simulation logic.
- Input handlers communicate movement intent to game entities.
- Maintains clean separation between control systems and physics systems.

Projectile Lifecycle Management

- Dynamically spawns projectile objects during runtime.
- Continuously tracks projectile positions.
- Automatically removes projectiles once they leave the visible viewport.
- Prevents unnecessary memory growth during extended sessions.

### TECHNICAL ARCHITECTURE

.
├── main.py
│   Primary simulation loop and runtime initialization
│
├── player.py
│   Player movement and rotation behavior
│
├── asteroid.py
│   Asteroid entity definitions and fragmentation logic
│
├── asteroidfield.py
│   Asteroid spawning and field management
│
├── shot.py
│   Projectile creation and movement
│
├── circleshape.py
│   Shared collision and geometric calculations
│
├── constants.py
│   Global simulation constants and configuration values
│
└── assets/
    Supporting graphical resources

### CORE ENGINEERING CONCEPTS DEMONSTRATED
Object-Oriented Programming

- Classes
- Inheritance
- Encapsulation
- Polymorphism
- Composition

Simulation Engineering

- Deterministic game loops
- Delta-time integration
- Real-time state management
- Dynamic object creation and destruction

Mathematics

- Vector arithmetic
- Distance calculations
- Angular rotation
- Coordinate transformations

Software Design

- Separation of concerns
- Reusable entity hierarchies
- Modular architecture
- Low-coupling component design

### DEPLOYMENT & LOCAL EXECUTION
1. Install Dependencies

pip install pygame

2. Clone Repository

git clone https://github.com/bharathc10/asteroids.git

3. Enter Project Directory

cd asteroids

4. Start Simulation

python3 main.py

### SIMULATION NAVIGATION CONTROLS
Angular Rotation

A / D
or
Left / Right Arrow Keys

Kinetic Acceleration

W / S
or
Up / Down Arrow Keys

Projectile Discharge

Spacebar
