import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'g-', animated=True, linewidth = 3)

x, y = [0,0.5,0.5,1,1.5,1.5,1.5,1.5,1.5,1,0.5,0.5,0.5,0.5,0.5,0.5,\
0.5,1,1.5,1.5,1.5,2,2.5,3,3.5,3.5,3.5,4,4.5,4.5,4.5,5,5.5,6,6.5,6.5,6.5,7,7.5,8,8], \
[0,0,0.5,0.5,0.5,1,1.5,2,2.5,2.5,2.5,3,3.5,4,4.5,5,5.5,5.5,5.5,6,6.5,6.5,6.5,6.5,6.5,\
7,7.5,7.5,7.5,8,8.5,8.5,8.5,8.5,8.5,9,9.5,9.5,9.5,9.5,10]

firex = [0,0,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0.5,0,0,0,0,0,0,0,4.5,0,0,0,0,0,0,0,5.5,0,0,0,0,0,0,0,0]
firey = [0,0,1.5,0,0,0,0,0,0,0,0,0,0,0,0,0,6.5,0,0,0,0,0,0,0,6.5,0,0,0,0,0,0,0,9.5,0,0,0,0,0,0,0,0]

obstaclex = [1.5,2.5,3.5]
obstacley = [3.5,5.5,8.5]
def init():
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):
    if(frame>=41):
        xdata.append(8)
        ydata.append(10)
    else:
        xdata.append(x[int(frame)])
        ydata.append(y[int(frame)])
    
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 80, 160),init_func=init, blit=True)

plt.plot(obstaclex,obstacley,"b*", label="Obstacle")
plt.plot(firex,firey,"r*", label="Fire")

plt.grid(True, linestyle = "-.", color = "b", linewidth = "1")
plt.legend(loc='lower right')
plt.show()