#! /usr/bin/env python

import sys
import os
import pymeshlab as ml
import trimesh


def mesh2glb(inname, outname):
    """Convert a mesh file to a GLB file.

    If the input file is in a format Trimesh supports, we load it with
    Trimesh and write out a GLB file.  Formats supported by Trimesh
    include STL, PLY, OBJ, OFF, GLB and GLTF.

    For formats not supported by Trimesh, particularly X3D and VRML 2.0,
    we use MeshLab to create an intermediate PLY file.  This PLY file
    is then passed to Trimesh to produce the final GLB.

    Note that in creating this PLY file, any scene hierarchy and non-mesh
    data such as camera, lights or animation are discarded.  All mesh
    objects in the scene graph are merged into one bundle of triangles.

    """

    words = inname.split('.')
    suffix = words[-1]

    tmpname = ""

    if suffix in trimesh.exchange.load.available_formats():
        # skip the meshlab stuff if trimesh supports in input format
        tmpname = inname
    else:
        # Use meshlab to read the mesh
        ms = ml.MeshSet()
        try:
            ms.load_new_mesh(inname)

            # remove the suffix of the input name
            dotpos = inname.rfind('.')
            if dotpos != -1:
                rootname = inname[0:dotpos]
            else:
                rootname = inname

            tmpname = rootname + '.ply'

            # Save a temporary PLY file
            ms.save_current_mesh(tmpname)
        except BaseException:
            print("Error: failed to load ", inname)
            sys.exit(1)

    try:
        tmesh = trimesh.load(tmpname)
    except BaseException:
        print("Error: failed to load ", tmpname)
        sys.exit(2)

    try:
        tmesh.export(outname)
    except BaseException:
        print("Error: failed to write ", outname)

    # Clean up the temp PLY file
    if tmpname != inname:
        os.remove(tmpname)


if __name__ == "__main__":

    inname = "teapot.wrl"
    outname = "teapot.glb"

    if len(sys.argv) > 1:
        inname = sys.argv[1]
        if len(sys.argv) > 2:
            outname = sys.argv[2]
        else:
            outname = inname.replace('.wrl', '.glb')

    print("Converting", inname, "to", outname)
    mesh2glb(inname, outname)
