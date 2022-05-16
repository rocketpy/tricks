import win32api
import win32con


# set position
tx, ty = 0, 0

# move mouse
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(tx/win32api.GetSystemMetrics(0)*65535),
                     int(ty/win32api.GetSystemMetrics(1)*65535) ,0 ,0)


# Hook and simulate mouse events on Windows and Linux
# https://github.com/boppreh/mouse

# pip install mouse
import mouse

# click left mouse  button
mouse.click('left')

# click right mouse button
mouse.click('right')

# click middle mouse button
mouse.click('middle')

# get position
print(mouse.get_position())
# width height

# Drag the mouse cursor 
# from (0,120) to (1000, 250) absolute screen in 1 sec
mouse.drag(0,120 , 1000, 250 , absolute=False, duration=1)

# Move the mouse cursor
# move to 1000px right and 500px down
mouse.move(1000,500, absolute=False, duration=1)

mouse.move(9,45)
# mouse.move(x, y, absolute=True, duration=0, steps_per_second=120.0)

# Check the mouse click, is_pressed() function
# click right button?
print(mouse.is_pressed("right"))

# click left button?
print(mouse.is_pressed("left"))

# click center button?
print(mouse.is_pressed("center"))

# mouse.drag(start_x, start_y, end_x, end_y, absolute=True, duration=0)
# mouse.click(button='left')
# mouse.double_click(button='left')
# mouse.on_button(callback, args=(), buttons=('left', 'middle', 'right', 'x', 'x2'), types=('up', 'down', 'double'))


# use on_click() and on_right_click() functions
import keyboard #pip install keyboard

#when left button click
mouse.on_click(lambda : print("Left button was clicked"))

#when right  button click
mouse.on_right_click(lambda : print("Right button was clicked"))

#press Esc to kill the event
if not keyboard.wait("Esc"):
    mouse.unhook_all()

# unhook_all() function will remove all the event listeners


# use wheel of the Mouse
# scroll wheel up
mouse.wheel(1)

# scroll wheel down
mouse.wheel(-1)
