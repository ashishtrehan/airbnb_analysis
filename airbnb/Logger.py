import logging, sys

def getLogger(name):

    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    log.addHandler(getHandler())
    return log

def getHandler():
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    return handler