import math
import numpy as np
theta = math.radians(45)
R_AB = np.asarray([math.cos(theta),-math.sin(theta),0,
                   math.sin(theta),math.cos(theta),0,
                   0,0,1
                  ]).reshape(3,3)
print(R_AB)