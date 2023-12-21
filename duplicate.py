from PIL import Image
import imagehash
import os
import numpy as np


def find_and_duplicates(images):
    similarity = 70
    hash_size = 8
    threshold = 1 - similarity / 100
    diff_limit = int(threshold * (hash_size**2))
    dup_map = {}

    for i in range(0, len(images)):
        dup_map[images[i]] = None
        with Image.open(images[i]) as img:
            hash1 = imagehash.average_hash(img, hash_size).hash

            for j in range(i + 1, len(images)):
                with Image.open(images[j]) as img:
                    hash2 = imagehash.average_hash(img, hash_size).hash

                    if np.count_nonzero(hash1 != hash2) <= diff_limit:
                        if dup_map[images[i]] == None:
                            dup_map[images[i]] = [images[j]]
                        else:
                            dup_map[images[i]] = dup_map[images[i]].append(images[j])
    dup_map = {k: v for k, v in dup_map.items() if v is not None}
    print(dup_map)

    return dup_map
