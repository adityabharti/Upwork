import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math
import time


frame = simplegui.create_frame("Home", 600,600)
canvas_width = 600
canvas_height = 600
ball_pos = []
ball_vel = []
ball_radius = 20
inner_track_radius = 150
outer_track_radius = 280
num_laps = 0
high_score = 0
over_half = False


def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

        
def draw(canvas):
    global over_half, num_laps, high_score
    mid = [canvas_width / 2, canvas_height / 2]
    
    canvas.draw_circle(mid, outer_track_radius, 1, "Aqua", "Black")
    canvas.draw_circle(mid, inner_track_radius, 1, "Aqua", "Green")
    canvas.draw_line((mid[0], mid[1] - inner_track_radius), (mid[0], mid[1] - outer_track_radius), 5, "White")
    canvas.draw_line((mid[0], mid[1] + inner_track_radius), (mid[0], mid[1] + outer_track_radius), 1, "White")
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    canvas.draw_circle(ball_pos, ball_radius, 1, "Red", "Red")
    canvas.draw_text("Laps:", [260, 230], 30, "Aqua")
    canvas.draw_text(str(num_laps), [290, 280], 30, "Aqua")
    canvas.draw_text("High Score:", [210, 340], 30, "Aqua")
    canvas.draw_text(str(high_score), [290, 390], 30, "Aqua")
    

    if distance(ball_pos, mid) > outer_track_radius - ball_radius or distance(ball_pos, mid) < inner_track_radius + ball_radius:
        reset()

    elif over_half and abs(ball_pos[0] - mid[0]) < ball_radius and ball_pos[1] < mid[1]:
        over_half = False
        num_laps += 1
        if num_laps > high_score:
            high_score = num_laps
    
    elif abs(ball_pos[0] - mid[0]) < ball_radius and ball_pos[1] > mid[1]:
        over_half = True

def reset():
    global ball_pos, ball_vel, num_laps, over_half
    ball_pos = [canvas_width / 2, canvas_height / 2 - (outer_track_radius + inner_track_radius) / 2]
    ball_vel = [0, 0]
    num_laps = 0
    over_half = False

def keydown_handler(key):
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        ball_vel[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        ball_vel[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        ball_vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        ball_vel[1] -= acc
    
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_canvas_background("Green")
frame.add_button("Reset", reset)

reset()
frame.start()