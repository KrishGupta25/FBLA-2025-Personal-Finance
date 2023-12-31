
class Format:
    end = '\033[0m'
    underline = '\033[4m'

text = Format.underline + "log in here" + Format.end
print(text)


