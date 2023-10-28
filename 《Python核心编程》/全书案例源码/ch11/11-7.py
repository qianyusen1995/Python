from PIL import Image
import numpy as np
 
foo = np.asarray(Image.open('/Users/aa/Desktop/照片/test.jpg').convert('L')).astype('float')
 
deep = 10.                      
grad = np.gradient(foo)             #取图像灰度的梯度值
gradX, gradY = grad               
gradX = gradX*deep/100.
gradY = gradY*deep/100.
F = np.sqrt(gradX**2 + gradY**2 + 1.)
uniX = gradX/F
uniY = gradY/F
uniZ = 1./F
 
lightEL = np.pi/2.2                   
lightAZ = np.pi/4.                    
dx = np.cos(lightEL)*np.cos(lightAZ)
dy = np.cos(lightEL)*np.sin(lightAZ)   
dz = np.sin(lightEL)              
 
b = 255*(dx*uniX + dy*uniY + dz*uniZ) 
b = b.clip(0,255)
 
im = Image.fromarray(b.astype('uint8')) 
im.save('/Users/aa/Desktop/照片/test2.jpg')