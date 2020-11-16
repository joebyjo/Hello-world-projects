import random
from Messages_bot import timetable


def random_color_generator(number_of_colors=120):
    color = ["0x"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(number_of_colors)]
    print(color)



bgchnwj = timetable()
print(bgchnwj.get_period())
print(bgchnwj.get_next_period())
