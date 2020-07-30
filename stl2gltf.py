#!/usr/bin/env python

import vtk

filename = "teapot.stl"

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)

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

writer = vtk.vtkGLTFExporter()
writer.SetFileName("teapot.glb")
writer.InlineDataOn()
writer.SetRenderWindow(renWin)
writer.Write()
