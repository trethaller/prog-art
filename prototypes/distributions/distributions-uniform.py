
import os
import random
import math
import cairo

width, height = 1000, 1000
radmin, radmax = 0.0001, 0.09



for seed in range(1000,1010):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.scale(width/2, height/2)
    context.translate(1,1)

    context.set_source_rgb(1,1,1)
    random.seed(seed)
    for i in range(300):
        context.arc(
            random.uniform(-1,1),
            random.uniform(-1,1),
            random.uniform(radmin, radmax),
            0, math.pi*2)
        context.fill()

    fname = 'uniform-%f-%f-seed-%s.png' % (radmin, radmax, seed)
    surface.write_to_png(fname)
    print(fname)
    #os.system(fname)
    #break
