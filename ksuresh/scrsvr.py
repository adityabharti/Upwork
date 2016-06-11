import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math
import time
svalue = 1


for i in range(0,9):
	frame = simplegui.create_frame("Home", 600,600)
	if svalue==1:
		print "Inside 1"
		message = "O"
		position = [50, 50]
		width = 500
		height = 500
		interval = 200
		radius = len(message)
		vel = [-5, 5]
		color = ["Red","Blue","Green","Yellow","White","Orange","Purple"]

		def update(text):
		    global message
		    message = text
		    global radius
		    radius = len(message)
		    
		def update1():
			global vel
			if vel[0]<0:
				vel[0]-=2
			else:
				vel[0]+=2

		def update2():
			global vel
			if vel[1]<0:
				vel[1]-=2
			else:
				vel[1]+=2			

		def update3():
			global vel
			if vel[0]<0:
				vel[0]+=2
			else:
				vel[0]-=2

		def update4():
			global vel
			if vel[1]<0:
				vel[1]+=2
			else:
				vel[1]-=2

		def chang():
			global svalue
			svalue = 2
			frame.stop()

		def reset():
			global vel
			vel[0] = -2
			vel[1] = 2

		def draw(canvas):
			position[0] += vel[0]
			position[1] += vel[1]

			if position[0] <= radius:
				vel[0] = -vel[0]

			if position[0] >= width-1:
				vel[0] = -vel[0]

			if position[1] <= radius:
				vel[1] = -vel[1]

			if position[1] >= height-1:
				vel[1] = -vel[1]


			color_value = random.randrange(0,len(color))

			canvas.draw_text(message, position, 36, color[color_value])


		

		text = frame.add_input("Message:", update, 150)

		frame.add_button("Increase horizontal speed\n",update1)
		frame.add_button("Decrease horizontal speed",update3)
		frame.add_button("Increase vertical speed",update2)
		frame.add_button("Decrease vertical speed",update4)

		frame.add_button("Reset", reset)
		frame.add_button("Change",chang)
		frame.set_draw_handler(draw)


		frame.start()

	elif svalue==2:

		print "Inside 2"
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

		def change():
			global svalue
			svalue = 1
			frame.stop()
		    
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

		frame.add_button("Change", change)
		reset()
		frame.start()

	else:
		print "INvalid"
		print