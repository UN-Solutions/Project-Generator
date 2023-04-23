import wordninja

example = 'hellothisisamazinglikereallycool'

def stringSplit(conString):
    print('test')
    result = wordninja.split(conString)
    result = " ".join(result)
    return result

solution = stringSplit(example)

print(solution)