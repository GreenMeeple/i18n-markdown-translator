from mdTranslate import mdTranslate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("f", help="markdown file to be translated", metavar="INPUT_FILE")
parser.add_argument("-s", default="en", help="Source language (default is en)", metavar="SOURCE_LANG")
parser.add_argument("-t", default="yue", help="Target language (default is yue)", metavar="TARGET_LANG")
args = parser.parse_args()


if __name__ == "__main__":
    mdTranslate(args.f, args.s, args.t)