
import os
import random
import math
import cairo

width, height = 1000, 1000
alpha = 1.161  # 80/20
invscale = 2000



for seed in range(1000,1010):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.scale(width/2, height/2)
    context.translate(1,1)

    context.set_source_rgb(1,1,1)
    random.seed(seed)
    for i in range(2000):
        context.arc(
            random.uniform(-1,1),
            random.uniform(-1,1),
            max((random.paretovariate(alpha)-1) / invscale, 1/width),
            0, math.pi*2)
        context.fill()

    fname = 'pareto-%f-%d-seed-%s.png' % (alpha, invscale, seed)
    surface.write_to_png(fname)
    #os.system(fname)
    #break
