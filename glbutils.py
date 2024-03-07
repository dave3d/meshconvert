import trimesh


def removeVertexColor(mesh):
    """Remove the vertex color from a mesh.

    All other vertex attributes are also removed.
    """

    mesh.visual.vertex_attributes.clear()


def setFaceColor(mesh, color):
    """Set all faces to a color."""

    cv = trimesh.visual.color.ColorVisuals(mesh, color, None)
    mesh.visual = cv


def getSceneMesh(scene):
    """Get the 1st mesh in a scene."""

    if type(scene) == trimesh.Trimesh:
        return scene

    try:
        if len(scene.geometry.items()) > 1:
            print("Warning: Scene has multiple meshes. Only 1st is returned.")

        for key, val in scene.geometry.items():
            # print(key, val)
            mesh = val
            return mesh
    except BaseException:
        print("Error: no mesh found")

    return None
