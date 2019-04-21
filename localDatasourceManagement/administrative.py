import json
import os


def createPutRequestFiles(dataDirectory, tableName):
    i = 1
    fileTracker = 1
    editedJSON = []
    fullJSON = {tableName:[]}
    finalJSONFile = open(str(tableName) + ".json", "w+")

    for fn in os.listdir(dataDirectory):
        if i <= 25:
            cjson = json.load(open(dataDirectory + fn))
            item = addTypestrings(cjson)
            editedJSON.append(item)
            i = i + 1
        else:
            fullJSON["runnerTry"] = editedJSON
            json.dump(fullJSON, finalJSONFile)
            finalJSONFile = open(str(tableName) + str(fileTracker) + ".json", "w+")
            fileTracker = fileTracker + 1
            editedJSON = []
            i = 1


def addTypestrings(cjson):
    for field in cjson:
        if 'str' in str(type(cjson[field])):
            cjson[field] = {"S": str(cjson[field])}
        elif 'int' in str(type(cjson[field])) or 'float' in str(type(cjson[field])):
            cjson[field] = {"N": str(cjson[field])}
        else:
            print("missing something HANNAH")
    item = {"PutRequest": {"Item": ""}}
    item["PutRequest"]["Item"] = cjson
    return item


# Loop through files & fields. Print all possible types to know how to format for dynamo
def collectTypes(folderDir):
    possibleTypes = set()

    for fn in os.listdir(folderDir):
        currentJSON = json.load(open(folderDir + fn))
        for field in currentJSON:
            possibleTypes.add(type(currentJSON[field]))

    print(possibleTypes)


if __name__ == "__main__":
    createPutRequestFiles("data/", "runnerTry")

