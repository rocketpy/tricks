# kitty - the fast, feature-rich, cross-platform, GPU based terminal

# https://github.com/kovidgoyal/kitty

# website - https://sw.kovidgoyal.net/kitty/

# Install - https://sw.kovidgoyal.net/kitty/

# Binary install
"""
You can install pre-built binaries of kitty if you are on macOS or Linux using the following simple command:

curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin

The binaries will be installed in the standard location for your OS, /Applications/kitty.app on macOS and ~/.local/kitty.app on Linux. 
The installer only touches files in that directory. To update kitty, simply re-run the command.


Warning !!!

Do not copy the kitty binary out of the installation folder. 
If you want to add it to your PATH, create a symlink in ~/.local/bin or /usr/bin or wherever. 
You should create a symlink for the kitten binary as well. 
Whichever folder you choose to create the symlink in should be in the systemwide PATH, 
a folder added to the PATH in your shell rc files will not work when running kitty from your desktop environment.
"""
