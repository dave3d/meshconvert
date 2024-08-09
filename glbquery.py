#! /usr/bin/env python

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
