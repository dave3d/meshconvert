
import trimesh

def removeVertexColor(mesh):
    """ Remove the vertex color from a mesh.

    All other vertex attributes are also removed.
    """

    mesh.visual.vertex_attributes.clear()

def setFaceColor(mesh, color):
    """ Set all faces to a color.
    """

    cv = trimesh.visual.color.ColorVisuals(mesh, color, None)
    mesh.visual = cv

