#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from pathlib import Path
from PIL import Image
from agentuniverse.agent.action.knowledge.reader.file.image_reader import ImageReader


class TestImageReader(unittest.TestCase):
    """Test cases for ImageReader."""

    def setUp(self):
        """Set up test fixtures."""
        self.reader = ImageReader()
        self.test_dir = Path(__file__).parent / "test_images"
        self.test_image = self.test_dir / "test.jpg"
        if not self.test_image.exists():
            raise FileNotFoundError(
                f"Test image not found at {self.test_image}. "
                f"Please place a test.jpg file in the {self.test_dir} directory."
            )

    def test_extract_text(self):
        """Test OCR text extraction."""
        image = Image.open(self.test_image)
        result = self.reader.extract_text(image)
        assert "Cute" in result

    def test_generate_description(self):
        """Test image description generation."""
        image = Image.open(self.test_image)
        result = self.reader.generate_description(image)
        assert "dog" in result

    def test_load_data(self):
        """Test successful data loading."""
        documents = self.reader._load_data(self.test_image)
        self.assertEqual(len(documents), 1)
        self.assertIn("Cute", documents[0].text)
        self.assertIn("dog", documents[0].text)
        self.assertEqual(documents[0].metadata['format'], 'jpg')
        self.assertTrue('image_size' in documents[0].metadata)
        self.assertTrue('channel' in documents[0].metadata)


if __name__ == '__main__':
    unittest.main()
