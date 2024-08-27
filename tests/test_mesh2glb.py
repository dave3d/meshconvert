#! /usr/bin/env python

""" Test for the mesh2glb function. """

import os
import tempfile
import unittest
import trimesh
from mesh2glb import mesh2glb

class TestMesh2Glb(unittest.TestCase):
    """ Class to test the mesh2glb function. """

    def setUp(self):
        """ Set up the testing dirctory and mesh. """
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.in_file = os.path.join(self.test_dir.name, "test.obj")
        self.out_file = os.path.join(self.test_dir.name, "test.glb")

        # Create a sample mesh file
        mesh = trimesh.creation.icosphere()
        mesh.export(self.in_file)

    def tearDown(self):
        """ Clean up the temporary directory. """
        # Cleanup the temporary directory
        self.test_dir.cleanup()

    def test_mesh2glb(self):
        """ Test the mesh2glb function. """
        # Call the mesh2glb function
        mesh2glb(self.in_file, self.out_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(self.out_file))

if __name__ == "__main__":
    unittest.main()
