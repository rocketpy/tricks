# keyboard - Hook and simulate keyboard events on Windows and Linux.
# Hook global events, register hotkeys, simulate key presses and much more.

# Homepage - https://github.com/boppreh/keyboard

# pip install keyboard

# to clone repo - git clone https://github.com/boppreh/keyboard

import keyboard


keyboard.press_and_release('shift+s, space')
keyboard.write('The quick brown fox jumps over the lazy dog.')
keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
keyboard.wait('esc')

# Record events until 'esc' is pressed.
recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.
keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# Block forever, like `while True`.
keyboard.wait()


# Use as standalone module:
# Save JSON events to a file until interrupted:
# python -m keyboard > events.txt

# cat events.txt
# {"event_type": "down", "scan_code": 25, "name": "p", "time": 1622447562.2994788, "is_keypad": false}
# {"event_type": "up", "scan_code": 25, "name": "p", "time": 1622447562.431007, "is_keypad": false}

# Replay events
# python -m keyboard < events.txt

