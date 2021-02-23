#! /usr/bin/env python

import sys
import os
import pymeshlab as ml
import ply2gltf

# This function converts a WRL file to GLTF in a 2 step process.
# First it goes from WRL to PLY using MeshLab, since MeshLab has
# a better WRL parser.  Then it converts from PLY to GLTF with
# the ply2gltf module, which uses VTK.  VTK supports GLTF writing,
# which MeshLab does not.
#
# Note that the function will actually work on any file format that
# MeshLab can read:  PLY, STL, OFF, OBJ, 3DS, VRML 2.0, X3D and COLLADA.
#
def wrl2gltf(inname, outname):

    # Use meshlab to read the WRL
    ms = ml.MeshSet()
    ms.load_new_mesh(inname)

    # Save a temporary PLY file
    ms.save_current_mesh('tempmesh.ply')

    ply2gltf.ply2gltf('tempmesh.ply', outname)

    # Clean up the temp PLY file
    os.remove('tempmesh.ply')


if __name__ == "__main__":

    inname = "teapot.wrl"
    outname = "teapot.gltf"

    if len(sys.argv) > 1:
        inname = sys.argv[1]
        if len(sys.argv) > 2:
            outname = sys.argv[2]
        else:
            outname = inname.replace('.wrl', '.gltf')

    print("Converting", inname, "to", outname)
    wrl2gltf(inname, outname)
