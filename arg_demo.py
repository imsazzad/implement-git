import argparse


def get_args():
    arggument_parser = argparse.ArgumentParser()
    arggument_parser.add_argument('-x', '--execute', action="store", required=True,
                                  help='Help text for option X')

    print(arggument_parser.parse_args())


if __name__ == '__main__':
    get_args()
