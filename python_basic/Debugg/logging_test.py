import logging
import sys

def do_stuff():
    logging.debug("In do_stuff")
    i = 5
    logging.debug("i = %d", i)
    return i
    logging.error("Code should not be reached!")

def main():
    logging.info("Program started")

if __name__ == "__main__":
    # Có thể comment dòng dưới để tắt debugging hoặc viết arg parser để thêm
    # option --debug khi chạy chương trình.
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # main()
    do_stuff()