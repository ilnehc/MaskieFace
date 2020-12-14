# Author: aqeelanwar
# Created: 27 April,2020, 10:22 PM
# Email: aqeel.anwar@gatech.edu

import argparse
import dlib
from utils.aux_functions import *


parser = argparse.ArgumentParser(
    description="Mask the face"
)
parser.add_argument(
    "--path",
    type=str,
    default="",
    help="Path to folder or images",
)
parser.add_argument(
    "--mask_type",
    type=str,
    default="surgical",
    choices=["surgical", "N95", "KN95", "cloth", "gas", "inpaint", "random", "all"],
    help="Type of the mask to be applied. Available options: all, surgical_blue, surgical_green, N95, cloth",
)

parser.add_argument(
    "--scale",
    type=int,
    default=1,
    help="scale 0 is low occultation, 1 is normal, 2 is high occulation",
)

parser.add_argument(
    "--verbose", dest="verbose", action="store_true", help="Turn verbosity on"
)
parser.add_argument(
    "--write_original_image",
    dest="write_original_image",
    action="store_true",
    help="If true, original image is also stored in the masked folder",
)
parser.set_defaults(feature=False)

args = parser.parse_args()
args.write_path = args.path + "_masked"

# Set up dlib face detector and predictor
args.detector = dlib.get_frontal_face_detector()  # Returns the default face detector
path_to_dlib_model = "dlib_models/shape_predictor_68_face_landmarks.dat"
if not os.path.exists(path_to_dlib_model):
    download_dlib_model()

args.predictor = dlib.shape_predictor(path_to_dlib_model)
is_directory, is_file, is_other = check_path(args.path)

if is_directory:
    path, dirs, files = os.walk(args.path).__next__()
    file_count = len(files)
    dirs_count = len(dirs)
    for f in tqdm(files):
        image_path = path + "/" + f

        write_path = path + "_masked"
        if not os.path.isdir(write_path):
            os.makedirs(write_path)

        if is_image(image_path):
            if args.verbose:
                str_p = "Processing: " + image_path
                tqdm.write(str_p)

            split_path = f.rsplit(".")
            masked_image, mask, mask_binary_array, original_image = mask_image(
                image_path, args
            )
            for i in range(len(mask)):
                w_path = (
                    write_path + "/" + split_path[0] + "_"
                    + mask[i] + "." + split_path[1]
                )
                img = masked_image[i]
                cv2.imwrite(w_path, img)

# Process if the path was a file
elif is_file:
    print("Masking image file")
    image_path = args.path
    write_path = args.path.rsplit(".")[0]
    if is_image(image_path):
        masked_image, mask, mask_binary_array, original_image = mask_image(
            image_path, args
        )
        for i in range(len(mask)):
            w_path = write_path + "_" + mask[i] + "." + args.path.rsplit(".")[1]
            img = masked_image[i]
            cv2.imwrite(w_path, img)
else:
    print("Path is neither a valid file or a valid directory")
print("Processing Done")
