
import random
from PIL import Image, ImageDraw
import numpy
import pylab


def gennoise(size):
    random.seed(0)
    for i in range(size):
        yield random.uniform(0,1)

def lowpass1(vals):
    v = 0.5
    for target in vals:
        v += (target - v) * 0.1
        yield v

def lowpass2(vals):
    d = 0
    v = 0.5
    for target in vals:
        d = (d + (target - v) * 0.01) * 0.98
        v += d
        v = max(0, min(1, v))
        yield v

def makefftgraph(vals, filename):
    fft = numpy.abs(numpy.fft.fft(vals))
    freqs = numpy.fft.fftfreq(len(vals))
    pylab.plot(freqs[1:], fft[1:], 'x')
    pylab.savefig(filename)
    pylab.close()


def makeimage(vals, filename):
    height = 100
    
    img = Image.new('RGB', (len(vals), height*2), 0xffffff)
    draw = ImageDraw.Draw(img)

    for i in range(len(vals)):
        val = vals[i]
        img.putpixel((i,height-int(val*height)), 0)
        draw.line((i,height,i,height*2), (int(val*255),)*3)

    img.save(filename)

'''
makeimage(list(gennoise(500)), 'noise.png')
makefftgraph(list(gennoise(5000)), 'noise-fft.png')

makefftgraph(list(lowpass1(gennoise(5000))), 'LP1-fft.png')
'''

#makeimage(list(gennoise(500)), 'noise.png')
#makeimage(list(lowpass1(gennoise(500))), 'LP1.png')
#makeimage(list(lowpass2(gennoise(500))), 'LP2.png')
#makefftgraph(list(lowpass2(gennoise(5000))), 'LP2-fft.png')
