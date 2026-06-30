#! /usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "trimesh",
# ]
# ///

""" Query a GLB file for information """

import sys
import trimesh
import glbutils

inname = sys.argv[1]

print("File:", inname)

scene = trimesh.load(inname)

mesh = glbutils.getSceneMesh(scene)

vsize = mesh.vertices.size
fsize = mesh.faces.size

print("Vertices: ", int(vsize / 3))
print("Triangles: ", int(fsize / 3))

if mesh.visual.defined:
    print("Color: ", mesh.visual.kind)
