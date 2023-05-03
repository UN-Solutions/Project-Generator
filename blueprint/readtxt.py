import csv
import json

def getText(textInputFile):
    # open txt file as a json
    with open(textInputFile, 'r') as f:
        inputTxt = json.load(f)
        return inputTxt

# main
if __name__ == "__main__":
    # get txt inputs
    example = getText('input.txt')
    print(example["phone"])