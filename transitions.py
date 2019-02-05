import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import pandas

a_x = 1
a_y = 1
s_x = 1
s_y = 2.5
r_x = 4
r_y = 1
e_x = 4
e_y = 2.5
w_x = 7
w_y = 1.5
d_x = 10
d_y = 2


def displayTransitionsExpl(dictrow, name):
    image = "interface.png"
    displayTransitions(dictrow, image, name)

def displayTransitionsBase(dictrow, name):
    image = "baseline.png"
    displayTransitions(dictrow, image, name)

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

def get_color(value):
    cmap = plt.cm.get_cmap('gist_heat')
    rgba = cmap(value/17.0)
    return rgba

def displayTransitions(dictRow, image, name):
    fig = plt.figure(frameon=False)
    img = imread(image)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, 11)
    ax.set_ylim(4, 0)
    ax.imshow(img, aspect='auto', extent=(0, 11, 0, 4), alpha=0.2, origin='lower', zorder=-1)
    ax.plot([a_x, s_x], [a_y, s_y], 'y-', linewidth=dictRow['a_s'], color=get_color(dictRow['a_s']))
    ax.plot([a_x, r_x], [a_y, r_y], 'y-', linewidth=dictRow['a_r'], color=get_color(dictRow['a_r']))
    ax.plot([a_x, e_x], [a_y, e_y], 'y-', linewidth=dictRow['a_e'], color=get_color(dictRow['a_e']))
    ax.plot([a_x, w_x], [a_y, w_y], 'y-', linewidth=dictRow['a_w'], color=get_color(dictRow['a_w']))
    ax.plot([a_x, d_x], [a_y, d_y], 'y-', linewidth=dictRow['a_d'], color=get_color(dictRow['a_d']))
    ax.plot([r_x, s_x], [r_y, s_y], 'y-', linewidth=dictRow['r_s'], color=get_color(dictRow['r_s']))
    ax.plot([r_x, e_x], [r_y, e_y], 'y-', linewidth=dictRow['r_e'], color=get_color(dictRow['r_e']))
    ax.plot([r_x, w_x], [r_y, w_y], 'y-', linewidth=dictRow['r_w'], color=get_color(dictRow['r_w']))
    ax.plot([r_x, d_x], [r_y, d_y], 'y-', linewidth=dictRow['r_d'], color=get_color(dictRow['r_d']))
    ax.plot([s_x, e_x], [s_y, e_y], 'y-', linewidth=dictRow['s_e'], color=get_color(dictRow['s_d']))
    ax.plot([s_x, w_x], [s_y, w_y], 'y-', linewidth=dictRow['s_w'], color=get_color(dictRow['s_w']))
    ax.plot([s_x, d_x], [s_y, d_y], 'y-', linewidth=dictRow['s_d'], color=get_color(dictRow['s_d']))
    ax.plot([e_x, w_x], [e_y, w_y], 'y-', linewidth=dictRow['e_w'], color=get_color(dictRow['e_w']))
    ax.plot([e_x, d_x], [e_y, d_y], 'y-', linewidth=dictRow['e_d'], color=get_color(dictRow['e_d']))
    ax.plot([w_x, d_x], [w_y, d_y], 'y-', linewidth=dictRow['w_d'], color=get_color(dictRow['w_d']))





    ax.set_axis_off()
    ax.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    set_size(11,4)
    fig.add_axes(ax)
    fig.savefig(name, bbox_inches='tight', pad_inches=0)
    plt.show()

df = pandas.read_csv('./mycsvfile.csv')
baseData = df[df['expl'] == False]
explData = df[df['expl'] == True]
sumBase = baseData.iloc[:, 10:].sum()
sumExpl = explData.iloc[:, 10:].sum()

print(sumBase)
print(sumExpl)


