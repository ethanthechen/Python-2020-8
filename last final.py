import tkinter as tk
import turtle
import time
import random

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_oval(x - self.radius, y - self.radius,
                                  x + self.radius, y + self.radius,
                                  fill='white')
        super(Ball, self).__init__(canvas, item)

    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

    def collide(self, game_objects):
        coords = self.get_position()
        x = (coords[0] + coords[2]) * 0.5
        if len(game_objects) > 1:
            self.direction[1] *= -1
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            coords = game_object.get_position()
            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1

        for game_object in game_objects:
            if isinstance(game_object, Brick):
                game_object.hit() 

class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 100
        self.height = 10         
        self.ball = None
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill='black')
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)

class Brick(GameObject):
    COLORS = {1:'yellow', 2: 'green', 3: '#222222'}
    def __init__(self, canvas, x, y, hits): 
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill=color, tags='brick')
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item,
                                   fill=Brick.COLORS[self.hits])

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width=self.width,
                                height=self.height,)
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle
        for x in range(5, self.width - 5, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind('<Left>',lambda _: self.paddle.move(-7))
        self.canvas.bind('<Right>',lambda _: self.paddle.move(7))


    def setup_game(self):
           self.add_ball()
           self.update_lives_text()
           self.text = self.draw_text(300, 200,'Press Space to start')
           self.canvas.bind_all('<space>',lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position() 
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size='24'):
        font = ('Forte', size)
        return self.canvas.create_text(x, y, text=text,
                                       font=font)

    def update_lives_text(self):
        text = 'Lives: %s' % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        self.canvas.unbind('<space>')
        self.canvas.delete(self.text)
        self.paddle.ball = None
        self.game_loop()

    def game_loop(self):
        self.check_collisions()
        num_bricks = len(self.canvas.find_withtag('brick'))
        if num_bricks == 0: 
            self.ball.speed = None
            self.draw_text(300, 200, 'You win!')
        elif self.ball.get_position()[3] >= self.height: 
            self.ball.speed = None
            self.lives -= 1
            if self.lives <= 0:
                self.draw_text(300, 200, 'You Lose you stupid son of Emir and Aaron')
            else:
                self.after(1000, self.setup_game)
        else:
            self.ball.update()
            self.after(50, self.game_loop)

    def check_collisions(self):
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        self.ball.collide(objects)










while True:
    print("1.Brick ball")
    print("2.snakc")
                                                



























































    print("4. exit system")
    sel = input("insert option: ")
    if sel == "1":
        if __name__ == '__main__':
            root = tk.Tk()
            root.title('ball hit brick')
            game = Game(root)
            game.mainloop()
    elif sel == "2":
        delay = 0.1

        # Score
        score = 0
        high_score = 0

        # Set up the screen
        #wn = window
        wn = turtle.Screen()
        wn.title("Snake Game understood by Stephen Han")
        wn.bgcolor("green")
        #Backround
        wn.setup(width=600, height=600)
        wn.tracer(0) # Turns off

        # Snake head
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")    
        head.color("black")
        head.penup()
        head.goto(0,0)
        head.direction = "stop"

        # Snake food
        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(0,100)

        segments = []

        # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

        # Functions
        def go_up():
            if head.direction != "down":
                head.direction = "up"

        def go_down():
            if head.direction != "up":
                head.direction = "down"

        def go_left():
            if head.direction != "right":
                head.direction = "left"

        def go_right():
            if head.direction != "left":
                head.direction = "right"

        def move():
            if head.direction == "up":
                y = head.ycor()
                head.sety(y + 20)

            if head.direction == "down":
                y = head.ycor()
                head.sety(y - 20)

            if head.direction == "left":
                x = head.xcor()
                head.setx(x - 20)

            if head.direction == "right":
                x = head.xcor()
                head.setx(x + 20)

        # Keyboard bindings
        wn.listen()
        wn.onkeypress(go_up, "Up")
        wn.onkeypress(go_down, "Down")
        wn.onkeypress(go_left, "Left")
        wn.onkeypress(go_right, "Right")

        # Main game loop
        while True:
            wn.update()

            # Check for a collision with the border
            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
        
                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


            # Check for a collision with the food
            if head.distance(food) < 20:
                # Move the food to a random spot
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                food.goto(x,y)

                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                segments.append(new_segment)

                # Shorten the delay
                delay -= 0.001

                # Increase the score
                score += 10

                if score > high_score:
                    high_score = score
        
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

            # Move the end segments first in reverse order
            #Body movement
            for index in range(len(segments) - 1, 0, -1):
                x = segments[index - 1].xcor()
                y = segments[index - 1].ycor()
                segments[index].goto(x, y)

            # Move segment 0 to where the head is
            #movement
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x,y)

            move()    

            # Check for head collision with the body segments
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"
        
                    # Hide the segments
                    #No more body
                    for segment in segments:
                        segment.goto(1000, 1000)
        
                    # Clear the segments list
                    segments.clear()

                    # Reset the score
                    score = 0

                    # Reset the delay
                    delay = 0.1
        
                    # Update the score display
                    pen.clear()
                    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            time.sleep(delay)

        wn.mainloop()

    elif sel=="3":
        print('Hello! What is your name?')
        myname = input()

        import random
        a = 1
        b = 1000
        num = random.randint(a,b)

        guesstaken = 0
        while guesstaken < 100:
            print('Hello ' + myname + " ,try to guess the number, it's between %d-%d" % (a,b))
            print('insert number:')
            ans = input()
            ans = int(ans)
            guesstaken = guesstaken + 1
            if ans < a or ans > b:
                print('the number is wrong')
            elif ans > num:          
                b = ans
            elif ans < num:
                a = ans
            elif ans == num:
       
                guesstaken = str(guesstaken)
                print('congrats, you got it right, you guessed the number in ' , guesstaken ,' guesses')
                break

       
       
    elif sel == "4":
        break
