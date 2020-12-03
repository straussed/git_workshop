import numpy as np
import pandas as pd

def get_kinematics(x, y):
<<<<<<< HEAD
	dx = q - q.shift()
	dy = z - z.shift()
=======
	dx = x - x.shift()
	dy = y - y.shift()
>>>>>>> parent of a529105... change x to q
	d2x = dx - dx.shift()
	d2y = dy - dy.shift()

	speed = np.sqrt(dx**2 + dy**2)
	acceleration = np.sqrt(d2x**2 + d2y**2)

	return speed, acceleration

def remove_outliers(data, m):
	d = np.abs(data - np.nanmedian(data))
    mdev = np.nanmedian(d)
    s = d/mdev if mdev else 0.
    
    return np.where(s < m)