import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

def set_size(w,h, ax=None):
    """ w, h: width, height in inches """
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

def generateMatrixExpl(nbA, nbR, nbW, nbD, nbS, nbE):
    matrix = np.random.random((5, 12))
    matrix[0] = np.array([nbA, nbA, nbR, nbR, nbR, nbR, nbW, nbW, nbW, nbW, nbD, nbD])
    matrix[1] = np.array([nbA, nbA, nbR, nbR, nbR, nbR, nbW, nbW, nbW, nbW, nbD, nbD])
    matrix[2] = np.array([nbS, nbS, nbE, nbE, nbE, nbE, nbW, nbW, nbW, nbW, nbD, nbD])
    matrix[3] = np.array([nbS, nbS, nbE, nbE, nbE, nbE, nbW, nbW, nbW, nbW, nbD, nbD])
    matrix[4] = np.array([nbS, nbS, nbR, nbR, nbR, nbR, 0, 0, 0, 0, nbD, nbD])
    return matrix

def createHeatmapExpl(matrix, name):
    img = 'interface.png'
    createHeatmap(matrix, img, name)

def createHeatmapBase(matrix, name):
    img = 'baseline.png'
    createHeatmap(matrix, img, name)

def createHeatmap(matrix, image, name):
    # alternative cmaps:
    # 'hot' https://matplotlib.org/examples/color/colormaps_reference.html
    # alternative bilinear is nearest to check
    fig = plt.figure(frameon=False)
    img = imread(image)
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(img, aspect='auto', extent=(0, 11, 0, 4), alpha=0.5, origin='lower', zorder=-1)
    ax.imshow(matrix, cmap='viridis', alpha=0.6, interpolation='bilinear', origin='lower', zorder=1)
    ax.set_axis_off()
    ax.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_xlim(0, 11)
    ax.set_ylim(4, 0)
    set_size(11,4)
    fig.add_axes(ax)


    fig.savefig(name, bbox_inches='tight', pad_inches=0)

    plt.show()



