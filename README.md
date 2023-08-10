# LSB Steganography Tool
This is a tool that uses LSB insertion in order to hide messages in an image. Built using Python and Pillow. This project was inspired by my learning about cybersecurity while studying for the CompTIA Security+ exam. It was built over the span of about 8 hours across 2 days. Much of this time was spent researching tools and methods in Python and Pillow. It is not intended by any means to be used seriously and I don't know how much more work I'll be doing on this. 

## What does it do?
It takes a 24 bit image and encodes a message using LSB insertion. Instead of only replacing the last bit:
> <u><b>Standard LSB Insertion</b></u>: Uses 8 bytes for 1 ASCII character (0-127)
> 
> 0100110<b>0</b>, 0010100<b>1</b>, 0101010<b>1</b> 0100110<b>0</b>, 0010100<b>1</b>, 0101010<b>0</b> 0100110<b>0</b>, 0010100<b>1</b>
> 
> 01101001 --- TO ASCII ---> 105 --- TO CHAR ---> "i" 

I decided to replace the last 3 bits in the first 2 bytes and the last 2 bits in the 3rd byte.
> <u><b>3:3:2 LSB Insertion</b></u>: Uses 3 bytes for 1 ASCII character (0-127)
> 
> 01001<b>011</b>, 00101<b>010</b>, 010101<b>01</b>
> 
> 01101001 --- TO ASCII ---> 105 --- TO CHAR ---> "i" 

Because 24 bit color images are used, I was able to take advantage of this by replacing larger chunks of the original RGB values. This allows for the storage of longer messages while keeping the original and modified images visually indiscernible from one another. The most obvious tell is the change in image format and thus, the increase in file size of the modified image.



## The <code>imgproc.py</code> file
aka "image processing"

This file contains several functions:
* <code>get_rgb_value_of_img()</code>: Takes the original image, pulls out the RGB values and passes them to <code>rgb_to_bin()</code>.
* <code>rgb_to_bin()</code>: Takes the RGB values from the original image, converts them into binary and stores them in a list. This function also handles adding any padding to ensure every value is 8 bits.
* <code>text_to_ascii()</code>: Takes the message text, converts each character into the ASCII code representation and stores these in a list.
* <code>text_ascii_to_bin()</code>: Takes the ASCII codes generated from the message and converts these into binary values. Also removes the "0b" prefix on all values and adjusts padding.
* <code>chunkify()</code>: Takes the binary representation of the message's ASCII values and breaks each byte into chunks. (3:3:2)
* <code>lsb_replacer()</code>: Takes the binary values of the original RGB colors and replaces the least significant bits with the chunks created by <code>chunkify()</code>. These new binary values are stored in a new list.
* <code>new_colors()</code>: Takes the new binary values created by <code>lsb_replacer()</code>,converts them into RGB values and stores them in a list.
* <code>pixel_replacer()</code>: Opens the original image and replaces the original set of RGB values with the new RGB values. This new image is then saved as a PNG so as to prevent the loss of data.


## The <code>decoder.py</code> file
This file contains the following functions:
* <code>get_rgb_value of img()</code>: Takes the modified image, pulls out the RGB values and passes them to <code>rgb_to_bin()</code>.
* <code>rgb_to_bin()</code>: Takes the RGB values from the original image, converts them into binary and stores them in a list. This function also handles adding any padding to ensure every value is 8 bits.
* <code>get_lsb()</code>: Takes the least significant bits (3:3:2) from the RGB values of the modified image, combines them to form the decoded binary and stores this value in a list. 
* <code>get_ascii()</code>: Transforms the decoded binary values into the associated character values based on their ascii code. Combines them to display the hidden message. This function stops when the ASCII value is equal to "126" or "~". This character is added to the hidden message to denote the end of the message.


## TODO
* A whole lot of code reorganization
* There is a cutoff for how long of a message you can embed but I haven't spent any time thinking about what that cutoff is or how to account for it. I imagine that you could just as easily replace the 3 LSBs of all bytes to increase storage size even more, though that would require more work since we would have to account for all final values that are not a multiple of 8.
