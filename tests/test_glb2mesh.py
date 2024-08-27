#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File: test_glb2mesh.py
# Created on: 2021-08-29 15:00:00
#

""" Test for the glb2mesh function. """
import os
import tempfile
import unittest
import trimesh
from glb2mesh import glb2mesh

class TestGlb2Mesh(unittest.TestCase):
    """ Class to test the glb2mesh function. """

    def setUp(self):
        """ Create the temporary directory and test GLB file. """
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.in_file = os.path.join(self.test_dir.name, "test.glb")
        self.out_file = os.path.join(self.test_dir.name, "test.x3d")

        # Create a sample GLB file
        mesh = trimesh.creation.icosphere()
        mesh.export(self.in_file)

    def tearDown(self):
        """ Remove all the temporary files. """
        # Cleanup the temporary directory
        self.test_dir.cleanup()

    def test_glb2mesh(self):
        """ Test the glb2mesh function. """
        # Call the glb2mesh function
        glb2mesh(self.in_file, self.out_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(self.out_file))

if __name__ == "__main__":
    unittest.main()
