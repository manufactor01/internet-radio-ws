UNDERSCORE = "_"
SPACE = " "
FILE_EXT = ".csv"

def process_url(url):
    SEP = "?u="
    url_list = url.split(SEP)
    return url_list[1]

def process_name(name):
    return name.replace('\"', '')

def generate_input_word(words):
    return SPACE.join(words)

def generate_csv_file_name(words):
    return UNDERSCORE.join(words) + FILE_EXT
