
def no_of_paint(wall_height, wall_width, wall_coverage):
    """This function returns the amount of paint neeeded
    for a give wall surface area"""
    import math
    result = math.ceil((wall_width*wall_height)/wall_coverage)
    return result


coverage = 5

height = float(input("What is the wall height:"))
width = float(input("What is the wall width:"))

can_to_buy = no_of_paint(wall_height=height, wall_width=width, wall_coverage=coverage)
print(f'You would need {can_to_buy} can(s) of paint')
