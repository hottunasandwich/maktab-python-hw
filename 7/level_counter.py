import logging

def level_counter(filename, level = logging.INFO):
    levels = [logging.ERROR, logging.DEBUG, logging.INFO, logging.WARNING, logging.WARN, logging.FATAL, logging.CRITICAL]
    counter = 0

    # checks if the level is in levels then raises and exception
    if level not in levels:
        raise Exception('Level object not found')   

    else:
        with open(filename) as f:
            for line in f:
                if logging.getLevelName(level) == line.split('|')[2].strip():
                    counter += 1


    return counter
            