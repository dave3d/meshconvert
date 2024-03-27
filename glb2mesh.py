#! /usr/bin/env python

import sys
import os
import pymeshlab as ml
import trimesh
import glbutils


def glb2mesh(inname, outname, removeColor=False, meshColor=None):
    """Convert a GLB file to other mesh formats.

    If the output format is supported by Trimesh, the GLB us loaded with
    Trimesh and written out with Trimesh.  Formats supported by Trimesh
    include STL, PLY, OBJ, OFF, GLB, and GLTF.

    For output formats not supported by Trimesh, particularly X3D and VRML 2.0,
    we use Trimesh to create an intermediate PLY file.  This PLY file is then
    passed to MeshLab to produce the final output file.

    Note that in creating this PLY file, any scene hierarchy and non-mesh
    data such as camera, lights or animation are discarded.  All mesh
    objects in the scene graph are merged into one bundle of triangles.
    """

    try:
        tmesh = trimesh.load(inname)
    except ValueException:
        print("Error: failed to load ", inname)
        sys.exit(1)

    print("Trimesh load:", inname)

    words = outname.split(".")
    suffix = words[-1]

    # tmesh could be a Scene, a Trimesh, or other types
    #
    mesh = glbutils.getSceneMesh(tmesh)

    if mesh == None:
        print("Warning: no mesh found")
        return

    if removeColor:
        print("Removing vertex color")
        glbutils.removeVertexColor(mesh)

    if meshColor != None:
        print("Setting face color:", meshColor)
        glbutils.setFaceColor(mesh, meshColor)

    if suffix in trimesh.exchange.load.mesh_formats():
        # Use trimesh to write the output mesh
        #
        try:
            mesh.export(outname)
        except ValueException:
            print("Error: failed to export", inname, "to", outname)
            sys.exit(2)
        print("Trimesh export:", outname)
        return

    else:
        # write out a PLY and then use MeshLab
        dotpos = inname.rfind(".")
        if dotpos != -1:
            rootname = inname[0:dotpos]
        else:
            rootname = inname
        tmpname = rootname + ".ply"

        mesh.export(tmpname)
        try:
            ms = ml.MeshSet()
            ms.load_new_mesh(tmpname)
            print("Meshlab load: ", tmpname)
        except ValueException:
            print("Error: Intermediate conversion failed.")
            sys.exit(3)

        try:
            ms.save_current_mesh(outname)
            print("Meshlab save: ", outname)
        except ValueException:
            print("Error: failed to save", outname)
            sys.exit(4)

        if tmpname != inname:
            os.remove(tmpname)


if __name__ == "__main__":

    inname = "teapot.glb"
    outname = "teapot.x3d"

    if len(sys.argv) > 1:
        inname = sys.argv[1]
        if len(sys.argv) > 2:
            outname = sys.argv[2]
        else:
            outname = inname.replace(".glb", ".x3d")

    print("Converting", inname, "to", outname)
    glb2mesh(inname, outname)
