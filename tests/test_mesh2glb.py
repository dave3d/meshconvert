#! /usr/bin/env python

import os
import tempfile
import unittest
import trimesh
from mesh2glb import mesh2glb

class TestMesh2Glb(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.in_file = os.path.join(self.test_dir.name, "test.obj")
        self.out_file = os.path.join(self.test_dir.name, "test.glb")

        # Create a sample mesh file
        mesh = trimesh.creation.icosphere()
        mesh.export(self.in_file)

    def tearDown(self):
        # Cleanup the temporary directory
        self.test_dir.cleanup()

    def test_mesh2glb(self):
        # Call the mesh2glb function
        mesh2glb(self.in_file, self.out_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(self.out_file))

if __name__ == "__main__":
    unittest.main()
