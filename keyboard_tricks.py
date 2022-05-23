# keyboard - Hook and simulate keyboard events on Windows and Linux.
# Hook global events, register hotkeys, simulate key presses and much more.

# Homepage - https://github.com/boppreh/keyboard

# pip install keyboard

import keyboard


keyboard.press_and_release('shift+s, space')
keyboard.write('The quick brown fox jumps over the lazy dog.')
keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))
