#!/usr/bin/python

import sys
import getopt


def main(argv):
    inputFile = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv, "hf:o:", ["ffile=", "ofile="])
        if len(opts) != 2:
            print(
                'Invalid command: \nUsage: python3 app.py -f <sql file> -o <output file>')
    except getopt.GetoptError:
        print('Invalid command: \nUsage: python3 app.py -f <sql file> -o <output file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: python3 app.py -f <sql file> -o <output file>')
            sys.exit()
        elif opt in ("-f"):
            inputFile = arg
        elif opt in ("-o"):
            outputFile = arg

    readFile(inputFile, outputFile)


def readFile(filePath, outputFile):
    try:
        linesListString = []
        with open(str(filePath), 'r') as fileObject:
            lines = fileObject.readlines()
            for line in lines:
                linesListString.append(line)
            parsingTableName(linesListString[0], linesListString, outputFile)

    except FileNotFoundError:
        print("File not found")
        sys.exit()


def parsingTableName(firstLine, rawData, outputFile):
    columnName = []
    rawName = firstLine.split("`")
    init = 0
    for column in rawName:
        if init % 2 != 0:
            if column != rawName[1]:
                columnName.append(column)
        init += 1

    name = rawName[1].capitalize()
    if name[-1] == 's':
        print('Plural name detected, consider to rename it after process done!')
    parsingData(name, columnName, rawData, outputFile)


def parsingData(tableName, columnName, rawData, outputFile):
    rawData.pop(0)
    listData = []
    for data in rawData:
        newData = '[' + data[1:-3] + ']'
        listData.append(newData)

    formingSeeder(tableName, columnName, listData, outputFile)


def formingSeeder(tableName, columnName, data, outputFile):
    # prepare data per column

    columnData = []
    for i in data:
        newData = i.split(",")
        newData[0] = newData[0].replace("[", "")
        newData[-1] = newData[-1].replace("]", "")
        columnData.append(newData)

    # create file
    fileName = outputFile.split(".")
    output = open(outputFile, "w")
    output.write('<?php\n\n')
    output.write('namespace Database\Seeders;\n\n\n')
    output.write('use Illuminate\Database\Seeder;\n')
    output.write('use App\Models\\' + tableName + ';\n\n')
    output.write('class ' + fileName[0] + ' extends Seeder\n{\n\n')
    output.write('\tpublic function run()\n\t{\n\n')
    output.write('\t\t$data = [\n')
    for i in columnData:
        count = 0
        output.write("\t\t\t[")
        for j in i:
            line = "'" + columnName[count] + "'" + "=>" + j + ","
            output.write(line + "\t")
            count += 1
        output.write("],\n")
    output.write('\t\t];\n')
    output.write('\t\t' + tableName + '::insert($data);\n')
    output.write('\t}\n')
    output.write('}\n')
    output.close()
    sys.exit()
