import numpy as np
import matplotlib.pyplot as plt
foo = np.arange(0, 10)
plt.plot(foo, np.square(foo), foo, foo*2, foo, np.sqrt(foo))
plt.show()