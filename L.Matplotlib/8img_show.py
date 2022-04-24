import matplotlib.pyplot as plt
import matplotlib.image as imp


plt.pie([40, 20, 30])
plt.savefig('Pie1')
img = imp.imread("Pie1.png")
print(img)                                          # gives 3 dimensional array output
# print(img.shape)
# print(img.ndim)
single_channel = img[:, :, 2]
plt.imshow(single_channel, cmap='twilight')              # shows the image in imp.imread()
# plt.axis('off')              # if axis is shown, it will remove
plt.colorbar()  # shows a color bar as side
plt.show()

