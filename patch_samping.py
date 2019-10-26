from matplotlib.image import imread
from matplotlib import pyplot as plt
import numpy as np


def read_image(file_name):
    image_matrix = imread(file_name)
    print(image_matrix.shape)
    return image_matrix


def output_image(image_arr):
    plt.imshow(image_arr, interpolation='nearest')
    plt.show()


def patch_sampling(image_arr, patch_width, patch_heigh, patch_distance):
    image_heigh = image_arr.shape[0]
    image_width = image_arr.shape[1]
    result = []
    for line_index in range(len(image_arr)):
        if line_index % patch_distance == 0:
            for each_pixel_index in range(len(image_arr[line_index])):
                if line_index + patch_heigh <= image_heigh and each_pixel_index + patch_width < image_width:
                    if each_pixel_index % patch_distance == 0:
                        patch_arr = image_arr[line_index:line_index+patch_heigh, each_pixel_index:each_pixel_index+patch_width]
                        result.append((patch_arr, (line_index, each_pixel_index)))
    return result

if __name__ == '__main__':
    patch_width = 224
    patch_heigh = 224
    patch_distance = 8
    data_size = 40
    result = []
    for i in range(1, 41):
        image_data = read_image("graph_data/Images/test_{}.png".format(i))
        annotation_data = read_image("graph_data/Annotation/test_{}.png".format(i))
        image_patch_result = patch_sampling(image_data, patch_width, patch_heigh, patch_distance)
        annotation_patch_result = patch_sampling(annotation_data, patch_width, patch_heigh, patch_distance)
        result.append((image_patch_result, annotation_patch_result))
    # result: an array, element: (origin_data, annotation_data), length=number of origin image
    # origin_data/annotation_data: an array, element: (patch_data, index_of_left_top_pixel), length=number of patch
    # patch_data: three dimension array
    # each patch_data in origin data should relate to the same index patch_data in annotation_data

