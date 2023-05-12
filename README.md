# A Unique Board Game: The Knight, The Football, and The Arguing King and Queen 

### Description:

In this game, you have two knights on each side of the board. There are 2 white knights, and there are 2 black knights. Each team has a football. In order to win, you must end up with your knight holding the football on the other side of the board/"endzone" (Just like a touchdown in football). There is one interesting catch though. On the middle row of the board, the king and queen can move freely along the horizontal. In the case in which they collide on any turn, the opposing team can not surpass their horizontal line while the king and queen resolve their argument. 

Rules
- The knights move exactly like knights in chess.
- Despite their names, the king and queen do not move like a king and queen in chess. They can only move one square at a time across the horizontal.
- No "incompletes" allowed. i.e., you cannot fling your football to the endzone and move your knight to the football. The football can only be passed between allied knights.
- A knight is in "posession" of a football after occupying the same square as the football. Once a knight possesses the ball, they can either move with it or pass it.
- During a turn, a player has the option to either move a knight, king, queen, or pass a ball. 
- After a king and queen collision, both white and black knights cannot move across the horizontal for an entire two full turns. (The person that made the queen and knight collide will still not be able to move their knight across the horizontal on their next turn. However, immediately on their turn following, the horizontal is freed and the queen and king are reset to their respective starting positions.)
- While the king and queen argue, footballs can still be passed across the horizontal. However, footballs cannot go through squares kings and queens occupy (nor knights, for that matter).
- Once an enemy knight is in a team's territory (past the horizontal) a knight can "capture" an enemy knight the exact same way the would in chess. In this case, the captured knight is sent back to their starting position. If that knight was in posession of a football, the football is sent back to its starting position as well.



### Helper Visualization (drawn on iPad): 


![IMG_0282](https://user-images.githubusercontent.com/61725820/217183146-843b2889-3030-4bc9-a670-d83d99e93418.jpg)


### Instructions:

1. Clone this repository and get it on your local machine.
2. Install all the neccesary dependencies to make a board game and test it. 

### Dependencies / Setup:

1. Python 3.6.5 (preferablly 3.8 or higher)
2. Pygame 
3. Numpy 

Use a virtual environment to install the dependencies. It is common in Python. Use Miniconda.

https://docs.conda.io/en/latest/miniconda.html

Sequence of conda actions: 

'conda create -n dylan_board_game python=3.8'

'conda info --envs'

'conda activate dylan_board_game'

'conda install numpy pytest'

