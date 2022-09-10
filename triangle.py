"""Triangle program core definitions"""

def start(args):
    """ Example for start """
    if len(args) != 7:
        print(f'Please provide 6 numbers in format point1x point1y point2x point2y point3x point3y ')
    else:
        point1 = (args[1],args[2])
        point2 = (args[3],args[4])
        point3 = (args[5],args[6])
        return f"Points are {point1} {point2} {point3}"
