def loadLang(langFile):
    readLang = langFile.readlines()

    output = {}
    for item in readLang:
        if item[0] != '#' and '=' in item:
            items = item.split('=')
            if items[1][-1] == '\n':
                items[1] = items[1][: -1]
            output[items[0]] = items[1]
    return output
