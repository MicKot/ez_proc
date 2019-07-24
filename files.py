import os
import numpy as np


def read_images_from_directory_into_buckets(dir, extensions=("jpg", "png", "jpeg")):

    buckets = []

    for root, dirs, files in os.walk(dir):
        if root == dir:
            continue
        paths = []
        for file in files:
            if file.endswith(extensions):
                full_path = os.path.join(root, file)
                paths.append(full_path)
        buckets.append(paths)
    return buckets
