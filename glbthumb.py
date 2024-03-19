#! /usr/bin/env python

import sys
import argparse
import numpy as np
import trimesh
import pyrender
import glbutils
import matplotlib.pyplot as plt


def bound_corners(bounds):
    corners = []
    for z in range(2):
        for y in range(2):
            for x in range(2):
                c = [bounds[x][0], bounds[y][1], bounds[z][2]]
                corners.append(c)
    return corners


def small_mesh_handler(mesh):
    """For some reason, generate_thumbnail produces a blank image for meshes
    with extents less than 1.0.  This function detects such meshes and scales
    them up to 100.0.  Yeah, it's an ugly hack.
    """

    size = max(mesh.bounding_box.primitive.extents)

    if size == 0.0:
        print("Warning: zero sized mesh")
        return

    if size < 1.0:
        scale = 100.0 / size
        print(f"Scaling small mesh by {scale:.2f}")
        scale_matrix = trimesh.transformations.scale_matrix(scale)
        mesh.apply_transform(scale_matrix)


def generate_thumbnail(inname, outname, light_color=[1.0, 1.0, 1.0]):
    """Generate a thumbnail image of a GLB mesh."""

    print("Loading", inname)
    tmesh_obj = trimesh.load(inname)

    mesh = glbutils.getSceneMesh(tmesh_obj)

    small_mesh_handler(mesh)

    if isinstance(mesh.visual, trimesh.visual.texture.TextureVisuals):
        cv = trimesh.visual.ColorVisuals(tmesh_obj)
        mesh.visual = cv

    corners = bound_corners(mesh.bounds)

    tm_scene = trimesh.scene.scene.Scene(geometry=[mesh])
    cam = tm_scene.camera
    cam_transform = cam.look_at(corners)

    pyren_mesh = pyrender.Mesh.from_trimesh(mesh)

    pyren_scene = pyrender.Scene()
    pyren_scene.add(pyren_mesh)

    pyren_cam = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.0)
    pyren_scene.add(pyren_cam, pose=cam_transform)

    pyren_light = pyrender.DirectionalLight(
        color=np.asarray(light_color), intensity=3.0
    )
    pyren_scene.add(pyren_light)

    r = pyrender.OffscreenRenderer(400, 400)
    color, depth = r.render(pyren_scene)

    plt.imsave(outname, color)

    print(outname, "written")


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    parser.add_argument(
        "--color",
        "-c",
        action="store",
        dest="color",
        help='Lighting color "1.0 1.0 1.0"',
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parseargs()

    print(args)

    inname = sys.argv[1]
    if len(args.filenames) == 0:
        print("Error: no input file")
        sys.exit(1)

    inname = args.filenames[0]

    if len(args.filenames) > 1:
        outname = args.filenames[1]
    else:
        rootname = inname[: inname.rfind(".")]
        outname = rootname + ".png"

    c = [1.0, 1.0, 1.0]
    if args.color:
        x = args.color.split(" ")
        c = [float(a) for a in x]

    print(c)
    generate_thumbnail(inname, outname, c)
