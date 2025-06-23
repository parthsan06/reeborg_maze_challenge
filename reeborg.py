# solution code for reeborg maze challenge
# link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# predefined functions in reeborg: turn_left, at_goal, front_is_clear, right_is_clear
def turn_right():
    for i in range(3):
        turn_left()
    
def navigate():
    while at_goal == False:
        turn_left()
        while right_is_clear() == False:
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear() == True:
            move()
        turn_left()
    
while at_goal() == False:
    navigate()
    if right_is_clear() == False and front_is_clear() == True:
        move()
    elif right_is_clear() == False and front_is_clear() == False:
        turn_left()
    else:
        turn_right()
        move()
