🏓 **Ping Pong Game in Python**
Welcome to the Ping Pong Game repository! This project features a classic Ping Pong game implemented using Python's turtle graphics library. The game provides an interactive experience for two players, where each player controls a paddle to hit a bouncing ball and score points by making the ball pass the opponent's paddle.

📜 **Overview**
This project is designed to showcase fundamental concepts in game development using Python. It leverages the turtle module to create a simple yet engaging game where players can compete against each other. The game mechanics include paddle movement, ball physics, collision detection, and scorekeeping.

⭐ **Features**
**Two-Player Mode:** Supports two players who can play against each other on the same keyboard.
**Interactive Gameplay:** Players use keyboard controls to move their paddles up, down, left, or right.
**Dynamic Ball Movement:** The ball bounces off the screen edges and paddles, with real-time direction changes.
**Scoring System:** Displays scores for both players and updates them as points are scored.
**Customizable Background:** Includes a customizable background image to enhance the visual experience.

**💻 Installation**
To get started with the Ping Pong game, follow these steps:

**1. Clone the Repository:**
```
git clone https://github.com/Harikantsharmag/ping-pong-game.git
```

**2. Navigate to the Project Directory:**
```
cd ping-pong-game
```

**3. Run the Game:** Ensure you have Python installed. Run the game using:
```
python ping_pong.py
```


**🎮 How to Play**
**Player 1 Controls:**
Move Up: W
Move Down: S
Move Left: A
Move Right: D

**Player 2 Controls:**
Move Up: Up Arrow
Move Down: Down Arrow
Move Left: Left Arrow
Move Right: Right Arrow

The objective of the game is to prevent the ball from passing your paddle and to score points by making the ball pass your opponent’s paddle. Each time the ball passes a paddle, the opposing player scores a point, and the ball resets to the center of the screen.

**🗂️ Code Structure**
**PingPong.py:** The main script containing the game logic, including paddle and ball movement, collision detection, and scoring.
**bg.png:** An optional background image that can be customized to enhance the visual appearance of the game.


**📝 Code Explanation**
The game is built using the turtle module, which provides basic graphics capabilities for Python. Key functions include:

**createBars():** Initializes the paddles and sets their positions.
**moveBar():** Handles paddle movement based on player input.
**moveBall():** Updates the ball’s position and direction.
**colDec():** Detects collisions between the ball and paddles.
**Scoring Logic:** Updates and displays scores when the ball passes a paddle.

**🤝 Contributing**
Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

**🗝️ License**
This project is licensed under the MIT License. See the LICENSE file for details.
