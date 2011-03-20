# set S-JTSK axes orientation

import matplotlib
matplotlib.use('GTKAgg')

import matplotlib.pyplot as plt


ax=plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])

# direction of axes
ax.invert_xaxis()
ax.invert_yaxis()

# ticks position
for tick in ax.xaxis.get_major_ticks():
        tick.label1On = False
        tick.label2On = True

for tick in ax.yaxis.get_major_ticks():
        tick.label1On = False
        tick.label2On = True

plt.plot([1,2,3,1],[3,1,2,3])

# ticks string formatter
import matplotlib.ticker as ticker
formatter = ticker.FormatStrFormatter('%.2f m')
ax.xaxis.set_major_formatter(formatter)

# ticks func formatter
def format(x, pos):
        return "%s - %s" % (x,pos)
formatter = ticker.FuncFormatter(format)
ax.xaxis.set_major_formatter(formatter)

plt.show()
