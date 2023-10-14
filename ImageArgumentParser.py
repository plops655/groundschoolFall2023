import argparse
from KMeansSegmentation import KDominantColors

def main(arguments):
    print("Starting main() function")
    parse_dominant = KDominantColors()
    print(parse_dominant.dominantColors(arguments.img_path))

# This if statement will take a path to an image if you attach the flag -ip before the call.
# It will then run the main function passing in the arguments as a list, so to access the image path, you must call arguments[0]
# You can import your solution and then call it in the main() function
# Example call in terminal to run this script: python3 ImageArgumentParser.py -ip "./test_images/color.png"
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', '--img_path', type=str, help='The path of the image you want to run color detection on.')
    args = parser.parse_args()
    main(args)