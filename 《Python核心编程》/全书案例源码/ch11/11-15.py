import numpy as np
import matplotlib.pyplot as plt
foo = np.arange(0, 10)
plt.plot(foo, np.square(foo), 'k:o', foo, foo*2, '-.+')
plt.show()