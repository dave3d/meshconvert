
import sys
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

def generate_thumbnail(inname, outname):
    """Generate a thumbnail image of a GLB mesh.
    """

    print("Loading", inname)
    tmesh_obj = trimesh.load(inname)

    mesh = glbutils.getSceneMesh(tmesh_obj)

    corners = bound_corners(mesh.bounds)

    tm_scene = trimesh.scene.scene.Scene(geometry=[mesh])
    cam = tm_scene.camera
    cam_transform = cam.look_at(corners)

    pyren_mesh = pyrender.Mesh.from_trimesh(mesh)

    pyren_scene = pyrender.Scene()
    pyren_scene.add(pyren_mesh)

    pyren_cam = pyrender.PerspectiveCamera( yfov=np.pi / 3.0, aspectRatio=1.0)
    pyren_scene.add(pyren_cam, pose=cam_transform)

    pyren_light = pyrender.DirectionalLight(color=np.ones(3), intensity=3.0)
    pyren_scene.add(pyren_light)

    r = pyrender.OffscreenRenderer(400,400)
    color, depth = r.render(pyren_scene)


    plt.imsave(outname, color)

    print(outname, "written")


if __name__ == '__main__':

    inname = sys.argv[1]

    if len(sys.argv)>2:
        outname = sys.argv[2]
    else:
        rootname = inname[:inname.rfind(".")]
        outname = rootname + '.png'

    generate_thumbnail(inname, outname)


