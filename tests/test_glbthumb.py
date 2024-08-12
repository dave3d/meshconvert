#! /usr/bin/env python

import os
import tempfile
import unittest
import trimesh
from glbthumb import generate_thumbnail

class TestGenerateThumbnail(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.in_file = os.path.join(self.test_dir.name, "test.glb")
        self.out_file = os.path.join(self.test_dir.name, "thumbnail.png")

        # Create a sample GLB file
        mesh = trimesh.creation.icosphere()
        mesh.export(self.in_file)

    def tearDown(self):
        # Cleanup the temporary directory
        self.test_dir.cleanup()

    def test_generate_thumbnail(self):
        # Call the generate_thumbnail function
        generate_thumbnail(self.in_file, self.out_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(self.out_file))

if __name__ == "__main__":
    unittest.main()
