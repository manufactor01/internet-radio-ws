import sys

from utils import generate_csv_file_name
from utils import generate_input_word
from internet_radio_ws import search_and_get_stations

SPACE = " "
MIN_WORDS = 2
MSG_NO_INPUT = "No input to search"

if __name__ == "__main__":
    if (len(sys.argv) < MIN_WORDS):
        raise(MSG_NO_INPUT)

    words = sys.argv
    words.pop(0)

    search_name = generate_input_word(words)
    file_name = generate_csv_file_name(words)
    search_and_get_stations(search_name, file_name)
