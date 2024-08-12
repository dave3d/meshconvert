
""" Utilities for working with glb files. """

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

    if isinstance(scene, trimesh.Trimesh):
        return scene

    if len(scene.geometry.items()) == 0:
        print("Error: no mesh found")
        return None

    try:
        if len(scene.geometry.items()) > 1:
            print("Warning: Scene has multiple meshes. Only 1st is returned.")

        first_item = next(iter(scene.geometry.items()))
        mesh = first_item[1]
        return mesh
    except ValueError:
        print("Error: no mesh found")

    return None
