from numpy import array as np_array, argwhere as np_argwhere


def crop_image(image):
    image_array = np_array(image)
    non_white_mask = image_array < 255
    non_white_pixels = np_argwhere(non_white_mask)
    if non_white_pixels.size == 0:
        return image
    top, left = non_white_pixels.min(axis=0)
    bottom, right = non_white_pixels.max(axis=0) + 1  # +1 to include the last pixel
    return image.crop((left, top, right, bottom))
