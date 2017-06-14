import sys
import os
import re
import struct


def get_image_size(path):
    with open(path, 'rb') as file:
        file.seek(16)
        data = file.read(8)
        return struct.unpack('>2L', data)


def main():
    if len(sys.argv) <= 1:
        print("Enter file name")
        sys.exit(0)

    path = sys.argv[1]
    if os.path.exists(path) is False:
        print("Invalid file name %s" % path)
        sys.exit(0)

    if re.match('\.png$', path, flags=re.IGNORECASE) is None:
        print("Path %s is not .png file" % path)
        sys.exit(0)

    width, height = get_image_size(path=path)
    print("The width of %s is %d x %d" % (path, width, height))


if __name__ == '__main__':
    main()
