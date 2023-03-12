# Answers:
# 1. What do you think the if does to the code under it?
# The if statement ensures that the code under it is only run if a certain condition is met. For example, the program will only run the line "print("Almost at the ball")" if the robot is behind the ball. 
# 2. What is the purpose indenting in the if statement? How can we tell what code is enclosed in an if branch and what code is not? 
# Indenting in the if statement allows us to easily tell which lines belong to which if statement. We know a code is enclosed in an if statement if it follows the if statement and is idented; otherwise, the code would not need to meet the condition of the if statement to run. 
#3. Done in program -- robot_location must be 5 less than ball location, and goal_location must be 90 less than ball_location.
#4. What do the operators += and -= do?
# += adds the value of the right operand to the left variable and assigns the new value to this variable. -= subtracts the value of the right operand from the left variable and assigns this new value to this variable.

robot_location = 100
ball_location = 105
goal_location = 90
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
