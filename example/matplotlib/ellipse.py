import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import FancyArrow


angles = [0, 45, 90] # degrees
ells = [Ellipse((1, 1), 4, 2, a) for a in angles]

#a = plt.subplot(111, aspect='equal')
a = plt.gca()

for e in ells:
    e.set_clip_box(a.bbox)
    e.set_alpha(0.1)
    a.add_artist(e)

plt.xlim(-1, 3)
plt.ylim(-1, 3)


# arrow
arr = FancyArrow(x=1, y=1, dx=1, dy=2, 
                 width=0.01, head_width=0.2, head_length=0.2,
                 length_includes_head=True)
a.add_artist(arr)

# text
a.text(1,1,"ABC", verticalalignment="top")

# equal aspect ratio
a.set_aspect("equal")

plt.show()

