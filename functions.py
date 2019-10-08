from gfxhat import lcd

#this function will create a vertical line across the gfxhat for 20 seconds.

def vertical_line(x,y):
    
 x = range(0,128)
  y = range(0,64)

 lcd.clear()
    x = random.randint(0,128)
    lcd.set_pixel(x,y = range(0,64),1)
lcd.show()
time.sleep(20)
lcd.clear() 
lcd.show()

from gfxhat import lcd

#this function will make a horizontal line across the gfxhat for 20 seconds.

def horizontal_line(x,y):
   
 x = range(0,128)
  y = range(0,64)
  lcd.clear()
    y = random.randint(0,64)
   lcd.set_pixel(y,x = range(0,128),1)
 lcd 
 lcd.show()
 time.sleep(20)
lcd.clear() 
lcd.show()

from gfxhat import lcd


#this function will create a staircase across the screen at a random x cordinate.
# h = horizontal v = vertical

def onestep(x,y,h=12,v=12,sh=128,sv=64)
x = range(0,128)
y = range(0,64)
x = random.randint(0,128)
for a in range(h):
    if x >= 0:
        lcd.set_pixel(x-i,y,1)
        else: a = h
for b in range(v):
    if y+b <= sv:

    else: b = v
return (x+h,y-v)
def staircase(x=12,y=12,h=6,v=6):
    while (x+h <128 and y-v >=0):
        x,y + onestep(x,y,h,v)
        lcd.clear()
        staircase()
        lcd.show()
lcd.clear()
lcd,show()

from gfxhat import lcd

#this function will make a single pixel pop up on the gfxhat then 5 seconds later 
#disappear off the screen and be replaced by a new pixel.

def pixel(x,y)

x = random.randint(0,128)
y = random.randint(0,64)
    
lcd.clear()
lcd.set_pixel(x,y,1)
lcd.show() 
time.sleep(5)
lcd.clear() 
lcd.show()

from gfxhat import lcd


#this function will set the whole screen ren then clear the gfxhat too get rid of all the pixels that are on the screen.

def backlightclear(x,y)
x = range(0,128)
y = range(0,64)
gfxhat.backlight.set_all(255,0,0)
lcd.clear() 
lcd.show()


