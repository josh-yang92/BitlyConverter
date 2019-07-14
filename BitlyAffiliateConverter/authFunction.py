import os


def getKeys(keyDir):
    file = open(os.path.join(keyDir, 'keys.txt'), 'r')
    fields = file.read()
    fields = fields.split('\n')
    keys = {}
    for items in fields:
        elements = items.split('=')
        keys[elements[0].strip()] = elements[1].strip()

    return keys
