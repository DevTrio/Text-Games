# An adventure game for Python 3.6.1 and above.
#
#  ________  ___    ___ _________  ___  ___  ________  ________      
# |\   __  \|\  \  /  /|\___   ___\\  \|\  \|\   __  \|\   ___  \    
# \ \  \|\  \ \  \/  / ||___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \   
#  \ \   ____\ \    / /     \ \  \ \ \   __  \ \  \\\  \ \  \\ \  \  
#   \ \  \___|\/  /  /       \ \  \ \ \  \ \  \ \  \\\  \ \  \\ \  \ 
#    \ \__\ __/  / /          \ \__\ \ \__\ \__\ \_______\ \__\\ \__\
#     \|__||\___/ /            \|__|  \|__|\|__|\|_______|\|__| \|__|
#          \|___|/                                                   
#                                                                   
#  ________  ________  ___      ___ _______   ________   _________  ___  ___  ________  _______      
# |\   __  \|\   ___ \|\  \    /  /|\  ___ \ |\   ___  \|\___   ___\\  \|\  \|\   __  \|\  ___ \     
# \ \  \|\  \ \  \_|\ \ \  \  /  / | \   __/|\ \  \\ \  \|___ \  \_\ \  \\\  \ \  \|\  \ \   __/|    
#  \ \   __  \ \  \ \\ \ \  \/  / / \ \  \_|/_\ \  \\ \  \   \ \  \ \ \  \\\  \ \   _  _\ \  \_|/__  
#   \ \  \ \  \ \  \_\\ \ \    / /   \ \  \_|\ \ \  \\ \  \   \ \  \ \ \  \\\  \ \  \\  \\ \  \_|\ \ 
#    \ \__\ \__\ \_______\ \__/ /     \ \_______\ \__\\ \__\   \ \__\ \ \_______\ \__\\ _\\ \_______\
#     \|__|\|__|\|_______|\|__|/       \|_______|\|__| \|__|    \|__|  \|_______|\|__|\|__|\|_______|
#
# art generated from http://patorjk.com/software/taag/#p=display&f=3D-ASCII&t=Python%0AAdventure

#strings:
directions = ["Head north", "Head south", "Head east", "Head west"]
birdStatue = ["Save", "Map", "Warp", "Save and Quit"]
currSave = open("currentSave.txt", "r")
location = open("./data/" + currSave.readline() + "/location.txt", "w+")
location.write("mainField")
print("you stand in a large field...")
