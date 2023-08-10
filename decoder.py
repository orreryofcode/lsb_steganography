from PIL import Image

original_img_bins = [];
decoded_bins = [];

def get_ascii():
    message = "";
    for i in range(len(decoded_bins)):
        ascii_code = int(decoded_bins[i], 2);
        if ascii_code == 126:
            break
        else:
            message += chr(ascii_code);

    print(message);

def get_lsb():

    count = 0;
    while count < len(original_img_bins):
        chunk_a = original_img_bins[count];

        chunk_b = original_img_bins[count + 1];

        chunk_c = original_img_bins[count + 2];

        completed_chunk = chunk_a[len(chunk_a) - 3:] + chunk_b[len(chunk_b) - 3:] + chunk_c[len(chunk_c) - 2:]
        decoded_bins.append(completed_chunk);

        count = count + 3;

def rgb_to_bin(rgb_value):

    # Convert RGB value to binary
    for color in rgb_value:
        binary_value = bin(color)[2:];

        # Add padding for MSB
        if len(binary_value) < 8:
            binary_value = binary_value.rjust(8, '0');


        original_img_bins.append(binary_value);

def get_rgb_value_of_img(img_path):
    img = Image.open(img_path);
    img_w = img.width; # should be img.width
    img_h = img.height; #should be img.height

    row = 0; # Top left Corner of Image;

    while row < img_w:
        col = 0;

        while col < 1:
            rgb_val = img.getpixel((row, col));

            rgb_to_bin(rgb_val);
            col = col + 1;

        row = row + 1;

get_rgb_value_of_img("modified.png");
get_lsb()
get_ascii()








