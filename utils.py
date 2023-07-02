def process_url(url):
    SEP = "?u="
    url_list = url.split(SEP)
    return url_list[1]

def process_name(name):
    return name.replace('\"', '')
