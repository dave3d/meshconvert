
import sys
import numpy as np
import trimesh

def generate_thumbnail(inname, outname):
    """Generate a thumbnail image of a GLB mesh.
    """

    print("Loading", inname)
    mesh = trimesh.load(inname)

    if type(mesh) == trimesh.Trimesh:
        scene = mesh.scene()
    elif type(mesh) == trimesh.Scene:
        scene = mesh

    fov = np.array([60,60])
    res = np.array([500,500])
    scene.camera.fov = fov
    scene.camera.resolution = res

    print("Bounds:", scene.bounds)
    print("Camera:", scene.camera)
    try:
        # save a render of the object as a png
        png = scene.save_image(resolution=[500, 500], visible=True)
        with open(outname, 'wb') as f:
            f.write(png)
            f.close()

    except BaseException as E:
        print("unable to save image", str(E))

    print(outname, "written")


if __name__ == '__main__':

    inname = sys.argv[1]

    if len(sys.argv)>2:
        outname = sys.argv[2]
    else:
        rootname = inname[:inname.rfind(".")]
        outname = rootname + '.png'

    generate_thumbnail(inname, outname)


