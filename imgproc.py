from PIL import Image, UnidentifiedImageError

original_img_bins = []
message_ascii_vals = []
message_bin_vals = []
message_chunks = []
new_bin_values = []
new_rgb_values = []


def pixel_replacer(img_path):
    img = Image.open(img_path)  # open image
    pixelmap = img.load()  # load pixel map
    img_w = img.width
    img_h = img.height
    rgb = []

    i = 0
    length = len(new_rgb_values)
    for value in new_rgb_values:
        if i < length:
            chunk_a = new_rgb_values[i]
            chunk_b = new_rgb_values[i + 1]
            chunk_c = new_rgb_values[i + 2]

            rgb.append((chunk_a, chunk_b, chunk_c))

        i += 3

    count = 0
    for j in range(img_w):
        for k in range(img_h):
            if count < len(rgb):
                pixelmap[k, j] = rgb[count]

                count += 1
            else:
                break

    img.save("modified.png")
    print("Modified image was saved.")
    return 1


def new_colors():
    for value in new_bin_values:
        color = int(value, 2)
        new_rgb_values.append(color)


def lsb_replacer():
    start = 0
    for value in message_chunks:
        idx = message_chunks.index(value, start)
        value_length = len(value)

        rgb_bin = original_img_bins[idx]
        new_rgb = rgb_bin[:len(rgb_bin) - value_length]

        new_rgb = new_rgb + value

        new_bin_values.append(new_rgb)
        start += 1


def chunkify():
    for value in message_bin_vals:
        message_chunks.append(value[:3])
        message_chunks.append(value[3:6])
        message_chunks.append(value[6:])


def text_ascii_to_bin():
    for code in message_ascii_vals:
        processed = bin(code)[2:]
        message_bin_vals.append(processed.rjust(8, '0'))

    chunkify()


def text_to_ascii(text=None):

    try:
        if text is None or len(text) < 1:
            return "Please include a message."

        for c in text:
            character = ord(c)
            if character <= 127:
                message_ascii_vals.append(character)
            else:
                return "Text ASCII value must be less than or equal to 127"
    except TypeError:
        return "TypeError: Message must be of type string."


def rgb_to_bin(rgb_value):
    # Convert RGB value to binary
    for color in rgb_value:
        binary_value = bin(color)[2:]

        # Add padding for MSB
        if len(binary_value) < 8:
            binary_value = binary_value.rjust(8, '0')

        original_img_bins.append(binary_value)


def get_rgb_value_of_img(img_path=None):
    if img_path is None or len(img_path) == 0:
        return "Please provide a JPEG image."

    try:
        img = Image.open(img_path)

        if img.format != "JPEG":
            img.close()
            return "Please provide a JPEG image."

        else:
            img_w = img.width
            img_h = img.height

            row = 0  # Top left Corner of Image;

            while row < img_w:
                col = 0

                while col < img_h:
                    rgb_val = img.getpixel((row, col))
                    rgb_to_bin(rgb_val)
                    col += 1

                row += 1

            img.close()

    except UnidentifiedImageError:
        return "File is not an image. Please use a JPEG image."


def lsb_encode(original_img=None, message=None):
    if original_img is None:
        original_img = input("Please enter the complete file path of the JPEG image you would like to encode: ")

    if message is None:
        message = input("Please type a message: ")

    if len(original_img) > 0:
        try:
            get_rgb_value_of_img(original_img)
            message += "~"
            text_to_ascii(message)
            text_ascii_to_bin()
            lsb_replacer()
            new_colors()
            pixel_replacer(original_img)
        except FileNotFoundError:
            print("File not found")
            return "File not found"
    else:
        print("No image provided")
        return "No image provided"
