# =========================+ Main +========================= #   
def level1_stalin_movement(event):
    if cp == True:
        global l1s_circ1, l1s_r1, l1s_r2, l1p1_circ1, l1p2_circ1, l1p3_circ1
        if event.key == "a":
            print("a")
            ls_circ1.move(-4,0)
            l1s_r1.move(-4,0)
            l1s_r2.move(-4,0)
            l1p1_circ1.move(-4,0)
            l1p2_circ1.move(-4,0)
            l1p3_circ1.move(-4,0)
        if event.key == "d":
            print("d")
            ls_circ1.move(4,0)
            l1s_r1.move(4,0)
            l1s_r2.move(4,0)
            l1p1_circ1.move(4,0)
            l1p2_circ1.move(4,0)
            l1p3_circ1.move(4,0)
    else:
        pass
add_key_down_handler(level1_stalin_movement)


def start_screen():
    start_background()  
    start_button()
    start_title()
    
def instruction_screen():
    instruction_background()
    instruction_title()
    instruction_direction()
    instruction_continue()
    
def level1_screen():
    global points, win, l1e1h
    level1_background()
    level1_stalin()
    level1_pellet1()
    level1_pellet2()
    level1_pellet3()
    level1_pellet_bar()
    level1_enemy()
    timer.set_interval(level1_enemy_movement,100)


# =========================+ Main +========================= #    
start_screen()

def start_program(x, y):
    global sp, cp
    if sp == True:
        if sb_r1.contains_point(x, y):
            remove_all()
            instruction_screen()
            sp = False
            cp = True
        else:
            pass
add_mouse_click_handler(start_program)

def continue_program(x, y):
    global cp
    if cp == True:
        if ic_r1.contains_point(x, y):
            remove_all()
            level1_screen()
        else:
            pass
add_mouse_click_handler(continue_program)

## level2_background()
## level2_stalin()
## level2_pellet1()
## level2_pellet2()
## level2_pellet3()
## level2_pellet_bar()
## level2_count1()
## level2_count2()
## level2_count3()
