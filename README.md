# mesh-convert

Try mesh to GLB conversion in Google Colab[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dave3d/meshconvert/blob/master/mesh2glb.ipynb)

Mesh conversion pipelines for use in NIH 3D workflows.  NIH 3D uses GLB as its main format.  
This repo provides a script to go from meshes to GLB, and another to go from GLB to other mesh
formats.  The other mesh formats include STL, PLY, OBJ, WRL and X3D.  Basically whatever
formats Trimesh or PyMeshLab support.

X3D and WRL are the two formats that PyMeshLab are used for, since Trimesh does not
support them.  Going between PyMeshLab and Trimesh, PLY is used as an intermediary format.
Because PLY is a relatively simple format, many features could be lost in translation.  In
particular and scene graph hierarchy, lighting or viewing parameters, or animation. 

The GLB thumbnail creation example (work-in-progress):
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dave3d/meshconvert/blob/master/thumbnail-example.ipynb)
