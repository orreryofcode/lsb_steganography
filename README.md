# LSB Steganography Tool
This is a tool that uses LSB insertion in order to hide messages in an image. It takes a 24 bit image and encodes a message using a 3:3:2 pattern of LSB insertion. Built using Python and Pillow. This project was inspired by my learning about cybersecurity while studying for the CompTIA Security+ exam.

## TODO
* A whole lot of code reorganization


## The <code>imgproc.py</code> file
This file contains several functions:
* <code>get_rgb_value_of_img</code>: Takes the original image, pulls out the RGB values and passes these values to...
* <code>rgb_to_bin</code>: Takes the RGB values from the original image, converts them into binary and stores them in a list. This function also handles adding any padding to ensure every value is 8 bits.
* <code>text_to_ascii</code>: Takes the message text, converts each character into the ascii code representation and stores these in a list.
* <code>text_ascii_to_bin</code>: Takes the ascii codes generated from the message and converts these into binary values. Also removes the "0b" prefix on all value and adjusts padding.
* <code>chunkify</code>: Takes the binary representation of the message's ascii values and breaks each byte into chunks. (3:3:2)
* <code>lsb_replacer</code>: Takes the binary values of the original RGB colors and replaces the least significant bits with the chunks created by <code>chunkify</code>. These new binary values are stored in a new list.
* <code>new_colors</code>: Takes the new binary values created by <code>lsb_replacer</code>,converts them into RGB values and stores them in a list.
* <code>pixel_replacer</code>: Opens the original image and replaces the original set of RGB values with the new RGB values. This new image is then saved as a PNG so as to prevent the loss of data.


## The <code>decoder.py</code> file
This file contains the following functions:
* <code>get_rgb_value of img</code>: Takes the modified image, pulls out the RGB values and passes these values to...
* <code>rgb_to_bin</code>: Takes the RGB values from the original image, converts them into binary and stores them in a list. This function also handles adding any padding to ensure every value is 8 bits.
* <code>get_lsb</code>: Takes the least significant bits (3:3:2) from the RGB values of the modified image, combines them to form the decoded binary and stores this value in a list. 
* <code></code>: Transforms the decoded binary values into the associated character values based on their ascii code. Combines them to display the hidden message. This function stops when the ASCII value is equal to "126" or "~". This character is added to the hidden message to denote the end of the message.

