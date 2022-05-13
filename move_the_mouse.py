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

mouse.move(9,45)
# mouse.move(x, y, absolute=True, duration=0, steps_per_second=120.0)

# mouse.drag(start_x, start_y, end_x, end_y, absolute=True, duration=0)

# mouse.click(button='left')

# mouse.double_click(button='left')

# mouse.on_button(callback, args=(), buttons=('left', 'middle', 'right', 'x', 'x2'), types=('up', 'down', 'double'))


