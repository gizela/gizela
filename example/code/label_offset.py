import matplotlib
import matplotlib.transforms
from pylab import figure, show

from matplotlib.transforms import offset_copy
def offset(fig, ax, x, y):
    return offset_copy(ax.transData, fig, x=x, y=y, units='dots')

fig=figure()
ax=fig.add_subplot(111)

# plot some data
x = (3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3)
y = (2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5)
ax.plot(x,y,'.')

# add labels
trans=offset(fig, ax, 10, 5)
for a,b in zip(x,y):
    ax.text(a, b, '(%d,%d)'%(a,b), transform=trans)

show()

