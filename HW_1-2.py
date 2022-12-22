def direction(compass, angle):
    turns = angle // 45
    dirr = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    start_pos = dirr.index(compass)
    end_pos = (start_pos + turns) % len(dirr)
    return dirr[end_pos]

assert direction("S", 180) == "N"
assert direction("SE", -45) == "E"
assert direction("W", 495) == "NE"