
import xrayutilities_id01_functions as id01
import numpy as np
import xrayutilities as xu
from mayavi import mlab

d = '../h5_files/'
fname = '20161115_E16019.h5'

scan_no = 3
h5file = d + fname

# Reconstruction

nx, ny, nz = 100,100,100
qx, qy, qz, gint, gridder = id01.gridmap(h5file, scan_no, nx, ny, nz, angdelta=[0,45,0,0])
QX, QY, QZ = np.mgrid[qx.min():qx.max():1j*nx,
                     qy.min():qy.max():1j*ny,
                     qz.min():qz.max():1j*nz]
INT = xu.maplog(gint, 4.5, 0)

# Plotting

mlab.figure()
mlab.contour3d(QX, QY, QZ, INT, contours=10, opacity=.2)
# mlab.colorbar() makes it crash!
mlab.axes(nb_labels=5, xlabel='Qx', ylabel='Qy', zlabel='Qz')
mlab.title('SCAN:%i'%scan_no, size=0.5, height=0.9)
mlab.show()