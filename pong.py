# Implementation of classic arcade game Pong

import  SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
ball_pos=[WIDTH/2,HEIGHT/2]
paddle1_pos=[[0,HEIGHT],[0, HEIGHT-PAD_HEIGHT]]
paddle2_pos=[[WIDTH,HEIGHT],[WIDTH,HEIGHT-PAD_HEIGHT]]
paddle_vel=[0,4]
ball_vel = [-random.randrange(60, 180)/60,random.randrange(120, 240)/60]
Upkey=False
Downkey=False
Wkey=False
Skey=False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    if direction=="left":
        ball_vel = [-random.randrange(60, 180)/60,random.randrange(120, 240)/60]
    elif direction=="right":
        ball_vel = [random.randrange(60, 180)/60,random.randrange(120, 240)/60]
        
    ball_pos=[WIDTH/2,HEIGHT/2]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle_vel,ball_pos,ball_vell # these are numbers
    global score1, score2
    score1=0
    score2=0
    ball_vel = [-random.randrange(60, 180)/60,random.randrange(120, 240)/60]
    ball_pos=[WIDTH/2,HEIGHT/2]

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle_vel
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #collision with walls
    
    if ball_pos[0] <= (BALL_RADIUS+PAD_WIDTH):
        if (ball_pos[1]>paddle1_pos[1][1]) and (ball_pos[1]<paddle1_pos[0][1]):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0]=ball_vel[0]+0.1
            
            
        else:
            score2+=1
            spawn_ball("right")
            
    if ball_pos[0]>=(WIDTH-BALL_RADIUS-PAD_WIDTH):
        if (ball_pos[1]>paddle2_pos[1][1]) and (ball_pos[1]<paddle2_pos[0][1]):
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=ball_vel[0]-0.1
            
        else:
            score1+=1
            spawn_ball("left")
        
        
        
    if ball_pos[1]<=BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    if ball_pos[1]>=HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
        
     #keypress handling   
    if Upkey :
        if paddle2_pos[1][1]<=paddle_vel[1]:
            paddle2_pos=[[WIDTH,PAD_HEIGHT],[WIDTH,0]]
        else:
            paddle2_pos[0][1] -= paddle_vel[1]
            paddle2_pos[1][1]-=paddle_vel[1]
    if Downkey:
        if paddle2_pos==[[WIDTH,HEIGHT],[WIDTH,HEIGHT-PAD_HEIGHT]]:
            paddle2_pos=[[WIDTH,HEIGHT],[WIDTH,HEIGHT-PAD_HEIGHT]]
        else:
            paddle2_pos[0][1] += paddle_vel[1]
            paddle2_pos[1][1]+=paddle_vel[1]
    if Wkey:
        if paddle1_pos[1][1]<=paddle_vel[1]:
            paddle1_pos=[[0,PAD_HEIGHT],[0,0]]
        else:
            paddle1_pos[0][1] -= paddle_vel[1]
            paddle1_pos[1][1]-=paddle_vel[1]
        
    if Skey:
        if paddle1_pos[0][1]>=HEIGHT:
            paddle1_pos=[[0,HEIGHT],[0, HEIGHT-PAD_HEIGHT]]
        else:    
            paddle1_pos[0][1] += paddle_vel[1]
            paddle1_pos[1][1]+=paddle_vel[1]
       
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    #drawing scores
    canvas.draw_text("Score: "+str(score1), (100, 40), 30, 'White')
    canvas.draw_text("Score: "+str(score2), (450, 40), 30, 'White')
    
    #drawing paddle
    canvas.draw_polygon(paddle1_pos, 12, 'White')
    
    canvas.draw_polygon(paddle2_pos, 12, 'White')
        


def reset():
    new_game()
    pass
def keydown(key):
    global paddle_vel, paddle2_vel,paddle2_pos,paddle1_pos,Upkey,Downkey,Wkey,Skey
    
    if key==simplegui.KEY_MAP["down"]:
        Downkey=True
    elif key==simplegui.KEY_MAP["up"]:
        Upkey=True
    elif key==simplegui.KEY_MAP["w"]:
        Wkey=True
    else:
        Skey=True

            
    
        
   
def keyup(key):
    global paddle_vel,Upkey,Downkey,Wkey,Skey
    
    if key==simplegui.KEY_MAP["down"]:
            Downkey=False
    elif key==simplegui.KEY_MAP["up"]:
        Upkey=False
    elif key==simplegui.KEY_MAP["w"]:
        Wkey=False
    else:
        Skey=False

    
  
        


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button('Restart', reset)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
