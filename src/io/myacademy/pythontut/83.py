#Write a script that detects and prints out your monitor resolution.

import screeninfo

print("Height:", screeninfo.get_monitors()[0].height, ", Width:", screeninfo.get_monitors()[0].width)