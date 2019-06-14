import urllib.request

def read_text():
    quotes = open('/home/ambar/Documents/coding/python/personal/speech_recognition-m.txt')
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = 'http://www.wdylike.appspot.com/'
    query = { 'q' : text_to_check }
    url_values = urllib.parse.urlencode(query)
    full_url = url + '?' + url_values

    try:
        response = urllib.request.urlopen(full_url)
        output = response.read().decode()

        response.close()

        #if output == 'true':
        if "true" in output:
            print('Profanity Alert!!')
            #elif output == 'false': #b'false'
        elif "false" in output:
            print('This document has no curse words.')
        else:
            print('Could not scan the document properly.')
    except urllib.error.URLError as e:
        print(e)
        print(e.code)
        print(e.reason)
    except UnicodeError as e:
        print(e)

read_text()
