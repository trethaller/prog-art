
import os
import random
import math
import cairo
import datetime

width, height = 800, 800

def html_to_rgb(color):
    """ Convert #RRGGBB to (R, G, B) normalized between 0 and 1 """
    codes = (color[1:3], color[3:5], color[5:7])
    return tuple(int(c, 16) / 255. for c in codes)

random.seed(1000)

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
context = cairo.Context(surface)

context.translate(width/2., height/2.)
scale = min(width,height) / 2.
context.scale(scale, scale)

context.set_source_rgb(1,1,1)
context.paint()

#context.set_source_rgba(0,0,0,0.3)
context.set_source_rgba(*(html_to_rgb('#08A9C9') + (0.2,)))
#context.set_line_cap(cairo.LINE_CAP_ROUND)
#context.set_line_width(0.004)

for i in range(2000):
    context.arc(
        #random.uniform(-.8,.8),
        #random.uniform(-.8,.8),
        random.gauss(0, 0.25),
        random.gauss(0, 0.25),
        0.03,
        0, math.pi*2)
    #context.stroke()
    context.fill()

fname = 'gaussian-%s.png' % (datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H.%M.%S"))
surface.write_to_png(fname)
print(fname)
os.system(fname)
