from PIL import Image

original_img_bins = []
message_ascii_vals = []
message_bin_vals = []
message_chunks = []
new_bin_values = []
new_rgb_values = []


def pixel_replacer(img_path):
    img = Image.open(img_path)  # open image
    pixelMap = img.load()  # load pixel map
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

        i = i + 3

    count = 0
    for j in range(img_w):
        for k in range(img_h):
            if count < len(rgb):
                pixelMap[k, j] = rgb[count]

                count = count + 1
            else:
                break

    img.save("modified.png")
    print("Modified image was saved.")


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
        start = start + 1


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


def text_to_ascii(text):
    for c in text:
        message_ascii_vals.append(ord(c))


def rgb_to_bin(rgb_value):
    # Convert RGB value to binary
    for color in rgb_value:
        binary_value = bin(color)[2:]

        # Add padding for MSB
        if len(binary_value) < 8:
            binary_value = binary_value.rjust(8, '0')

        original_img_bins.append(binary_value)


def get_rgb_value_of_img(img_path):
    img = Image.open(img_path)

    img_w = img.width
    img_h = img.height

    row = 0  # Top left Corner of Image;

    while row < img_w:
        col = 0

        while col < img_h:
            rgb_val = img.getpixel((row, col))
            rgb_to_bin(rgb_val)
            col = col + 1

        row = row + 1

    img.close()


def init(original_file, message):
    get_rgb_value_of_img(original_file)
    test_string = message + "~"
    text_to_ascii(test_string)
    text_ascii_to_bin()
    lsb_replacer()
    new_colors()
    pixel_replacer(original_file)


init("gato.jpg", "Secret Message... Shhhh")
