ax = plt.gca()


theta = np.linspace(0, 2 * np.pi, 100)
r = 1
x = r * np.cos(theta)
y = r * np.sin(theta)

ax.plot(x, y)
plt.axis('scaled')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

circle1 = plt.Circle((0, 0), 0.2, color='r', fill=False)

ax=plt.gca()
ax.add_patch(circle1)
plt.axis('scaled')
plt.show()