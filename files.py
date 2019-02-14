import os
import numpy as np


def read_images_from_directory_into_buckets(dir, extensions=('jpg', 'png')):

    buckets = []

    for root, dirs, files in os.walk(dir):
        if root == dir:
            continue

        dir_path_list = []

        for file in files:
            if file.endswith(extensions):
                full_path = os.path.join(root, file)
                dir_path_list.append(full_path)

        else:
            array = np.stack(dir_path_list)
            buckets.append(array)

    return buckets