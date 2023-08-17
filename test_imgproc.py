import unittest
import imgproc


class TestImgProc(unittest.TestCase):
    def test_get_rgb_value_of_img(self):
        # Test that a parameter is passed
        self.assertEqual(imgproc.get_rgb_value_of_img(), "Please provide a JPEG image.")
        self.assertEqual(imgproc.get_rgb_value_of_img(""), "Please provide a JPEG image.")

        # Test that correct file extension is passed
        self.assertEqual(imgproc.get_rgb_value_of_img("cat.png"), "Please provide a JPEG image.")
        self.assertEqual(imgproc.get_rgb_value_of_img("test.txt"), "File is not an image. Please use a JPEG image.")
        self.assertEqual(imgproc.get_rgb_value_of_img("gato.jpg"), None)

    def test_text_to_ascii(self):
        # Test that message conforms to standard ASCII table
        self.assertEqual(imgproc.text_to_ascii("ぁ"), "Text ASCII value must be less than or equal to 127")

        # Test that message actually exists
        self.assertEqual(imgproc.text_to_ascii(""), "Please include a message.")
        self.assertEqual(imgproc.text_to_ascii(), "Please include a message.")

        # Test that message is a string
        self.assertEqual(imgproc.text_to_ascii("Hello world"), None)
        self.assertNotEqual(imgproc.text_to_ascii(123456), None)

    def test_lsb_encode(self):
        img_path = "gato.jpg"
        message = "Test message"

        self.assertEqual(imgproc.lsb_encode("asdf", "message"), "File not found")
        self.assertEqual(imgproc.lsb_encode("", "message"), "No image provided")
        self.assertEqual(imgproc.lsb_encode(img_path, message), None)


if __name__ == '__main__':
    unittest.main()
