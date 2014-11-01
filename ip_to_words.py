#-------------------------------------------------------------------------------
# Name:        ip_to_words
# Purpose:      turn iden
#
# Author:      User
#
# Created:     01/11/2014
# Copyright:   (c) User 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import logging
import os



def setup_logging(log_file_path):
    # Setup logging (Before running any other code)
    # http://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/
    assert( len(log_file_path) > 1 )
    assert( type(log_file_path) == type("") )
    global logger
    # Make sure output dir exists
    log_file_folder =  os.path.dirname(log_file_path)
    if log_file_folder is not None:
        if not os.path.exists(log_file_folder):
            os.makedirs(log_file_folder)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logging.debug('Logging started.')
    return


def import_list(listfilename="ERROR.txt"):
    if os.path.exists(listfilename):# Check if there is a list
        query_list = []# Make an empty list
        list_file = open(listfilename, 'rU')
        for line in list_file:
            if line[0] != '#' and line[0] != '\n':# Skip likes starting with '#' and the newline character
                if line[-1] == '\n':# Remove trailing newline if it exists
                    stripped_line = line[:-1]
                else:
                    stripped_line = line# If no trailing newline exists, we dont need to strip it
                query_list.append(stripped_line)# Add the username to the list
        list_file.close()
        return query_list
    else: # If there is no list, we're fucked
        logging.error("No wordlist!")
        return []


def append_list(lines,list_file_path="done_list.txt",initial_text="# List of words",overwrite=False):
    # Append a string or list of strings to a file; If no file exists, create it and append to the new file.
    # Strings will be seperated by newlines.
    # Make sure we're saving a list of strings.
    if ((type(lines) is type(""))or (type(lines) is type(u""))):
        lines = [lines]
    # Ensure file exists and erase if needed
    if (not os.path.exists(list_file_path)) or (overwrite is True):
        list_file_segments = os.path.split(list_file_path)
        list_dir = list_file_segments[0]
        if list_dir:
            if not os.path.exists(list_dir):
                os.makedirs(list_dir)
        nf = open(list_file_path, "w")
        nf.write(initial_text)
        nf.close()
    # Write data to file.
    f = open(list_file_path, "a")
    for line in lines:
        outputline = line+"\n"
        f.write(outputline)
    f.close()
    return


def de_hex(hex_string):
    """Read a string of hex code and pump out a integer representation"""
    # http://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python
    return int(hex_string, 16)



def assign_word(word_list,value):
    pass

def shorten_list(list_to_shorten,desired_length):
    assert (len(list_to_shorten) >= desired_length)# Can't shorten to less than what we have
    working_list = list_to_shorten
    results_list = []
    counter = 0
    while len(results_list) < desired_length:
        # keep every 10th word
        results_list.append(working_list.pop(counter*10))
        counter += 1
    return results_list


def main():
    word_list = import_list(listfilename="linuxwords.txt")
    logging.debug(repr(len(word_list)))
    short_list = shorten_list(list_to_shorten=word_list,desired_length=256)
    logging.debug(short_list)
    pass

if __name__ == '__main__':
    # Setup logging
    setup_logging(os.path.join("debug","ip_to_words_log.txt"))
    try:
        main()
    except Exception, err:
        # Log exceptions
        logger.critical("Unhandled exception!")
        logger.critical(str( type(err) ) )
        logging.exception(err)
    logging.info( "Program finished.")