import pgzrun


TITLE='FLAPPY BALL'
HEIGHT=600
WIDTH=600

GRAVITY=200


class Ball():
  def __init__(self):
      self.radius=45
      self.color="Blue"
      self.x=300
      self.y=100
      self.vx=30
      self.vy=0
  def make(self):
      screen.draw.filled_circle((self.x,self.y),self.radius,self.color) 
ball1=Ball()

def draw():
    screen.clear()
    ball1.make()
    
def update(dt):
    uy=ball1.vy
    ball1.vy+=GRAVITY*dt
    ball1.y+=(uy+ball1.vy)*0.5*dt
    if ball1.y>555:
        ball1.y=555
        ball1.vy=ball1.vy*-0.9
    if ball1.x<45 or ball1.x>555:
        ball1.vx=ball1.vx*-1
    ball1.x=ball1.x+(ball1.vx*dt)    
    if keyboard.space:
        ball1.vy=-500



pgzrun.go()