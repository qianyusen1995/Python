import matplotlib.gridspec as gridspec
foo = gridspec.GridSpec(3, 3)
plt.subplot(foo[0, 0])
plt.subplot(foo[0:2, 1])
plt.subplot(foo[0:, -1])
plt.subplot(foo[1, 0])
plt.subplot(foo[2, 0:2])
plt.show()
