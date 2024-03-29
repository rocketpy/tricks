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


# To Do
"""
# to lock Windows desktop
keyboard.send('win+l')

import ctypes,time,keyboard

dll = ctypes.WinDLL('user32.dll')
dll.LockWorkStation()

time.sleep(2)

keyboard.send('Enter')
keyboard.send('My password')
keyboard.send('Enter')

"""


# Use as standalone module:
# Save JSON events to a file until interrupted:
# python -m keyboard > events.txt

# cat events.txt
# {"event_type": "down", "scan_code": 25, "name": "p", "time": 1622447562.2994788, "is_keypad": false}
# {"event_type": "up", "scan_code": 25, "name": "p", "time": 1622447562.431007, "is_keypad": false}

# Replay events
# python -m keyboard < events.txt


# Common patterns and mistakes for Preventing the program from closing
import keyboard

keyboard.add_hotkey('space', lambda: print('space was pressed!'))
# If the program finishes, the hotkey is not in effect anymore.

# VERY IMPORTANT !!!
# Don't do this! This will use 100% of your CPU.
# while True: pass

# Use this instead
keyboard.wait()

# or this
import time

while True:
    time.sleep(1000000)


# Waiting for a key press one time
import keyboard

# VERY IMPORTANT !!!
# Don't do this! This will use 100% of your CPU until you press the key.
# while not keyboard.is_pressed('space'):
#     continue
# print('space was pressed, continuing...')

# Do this instead
keyboard.wait('space')
print('space was pressed, continuing...')


# Repeatedly waiting for a key press
import keyboard

# VERY IMPORTANT !!!
# Don't do this!
# This will use 100% of your CPU and print the message many times.

#while True:
#    if keyboard.is_pressed('space'):
#        print('space was pressed!')


# Do this instead
while True:
    keyboard.wait('space')
    print('space was pressed! Waiting on it again...')

# or this
keyboard.add_hotkey('space', lambda: print('space was pressed!'))
keyboard.wait()


# Invoking code when an event happens
import keyboard

# VERY IMPORTANT !!!
# Don't do this! This will call `print('space')` immediately then fail when the key is actually pressed.
#keyboard.add_hotkey('space', print('space was pressed'))

# Do this instead !!!
keyboard.add_hotkey('space', lambda: print('space was pressed'))

# or this
def on_space():
    print('space was pressed')
keyboard.add_hotkey('space', on_space)

# or this
while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
        print('space was pressed')

        
# 'Press any key to continue'

# VERY IMPORTANT !!!
# Don't do this! The `keyboard` module is meant for global events, even when your program is not in focus.
#import keyboard
#print('Press any key to continue...')
#keyboard.get_event()

# Do this instead
input('Press enter to continue...')

# Or one of the suggestions from here
# https://stackoverflow.com/questions/983354/how-to-make-a-script-wait-for-a-pressed-key


# API methods:
"""
    keyboard.KEY_DOWN
    keyboard.KEY_UP
    keyboard.KeyboardEvent
    keyboard.all_modifiers
    keyboard.sided_modifiers
    keyboard.version
    keyboard.is_modifier
    keyboard.key_to_scan_codes
    keyboard.parse_hotkey
    keyboard.send (aliases: press_and_release)
    keyboard.press
    keyboard.release
    keyboard.is_pressed
    keyboard.call_later
    keyboard.hook
    keyboard.on_press
    keyboard.on_release
    keyboard.hook_key
    keyboard.on_press_key
    keyboard.on_release_key
    keyboard.unhook (aliases: unblock_key, unhook_key, unremap_key)
    keyboard.unhook_all
    keyboard.block_key
    keyboard.remap_key
    keyboard.parse_hotkey_combinations
    keyboard.add_hotkey (aliases: register_hotkey)
    keyboard.remove_hotkey (aliases: clear_hotkey, unregister_hotkey, unremap_hotkey)
    keyboard.unhook_all_hotkeys (aliases: clear_all_hotkeys, remove_all_hotkeys, unregister_all_hotkeys)
    keyboard.remap_hotkey
    keyboard.stash_state
    keyboard.restore_state
    keyboard.restore_modifiers
    keyboard.write
    keyboard.wait
    keyboard.get_hotkey_name
    keyboard.read_event
    keyboard.read_key
    keyboard.read_hotkey
    keyboard.get_typed_strings
    keyboard.start_recording
    keyboard.stop_recording
    keyboard.record
    keyboard.play (aliases: replay)
    keyboard.add_word_listener (aliases: register_word_listener)
    keyboard.remove_word_listener (aliases: remove_abbreviation)
    keyboard.add_abbreviation (aliases: register_abbreviation)
    keyboard.normalize_name
"""
