#!/usr/bin/env python

import sys
import vtk

def ply2gltf(inname, outname):

    reader = vtk.vtkPLYReader()
    reader.SetFileName(inname)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)

    # Assign actor to the renderer
    ren.AddActor(actor)


    # Export the GLTF
    writer = vtk.vtkGLTFExporter()
    writer.SetFileName(outname)
    writer.InlineDataOn()
    writer.SetRenderWindow(renWin)
    writer.Write()

if __name__ == "__main__":

    inname = "teapot.ply"
    outname = "teapot.gltf"

    if len(sys.argv) > 1:
        inname = sys.argv[1]
        if len(sys.argv) > 2:
            outname = sys.argv[2]
        else:
            outname = inname.replace('.ply', '.gltf')

    print("Converting", inname, "to", outname)
    ply2gltf(inname, outname)
