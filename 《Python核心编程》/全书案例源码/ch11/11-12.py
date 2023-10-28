import numpy as np
import matplotlib.pyplot as plt

foo = np.arange(0, 10)
plt.subplot(2, 2, 1)
plt.plot(foo, np.square(foo))
plt.subplot(2, 2, 2)
plt.plot(foo, np.cos(foo))