# Imports of libs
import argparse
import os

parser = argparse.ArgumentParser(description="Amazon Drive Bypass ")
parser.add_argument('-m', '--method',  dest='method', type=str, choices=["hide", "recover"], help="Select Method", required=True)
parser.add_argument('-i', '--input', dest='inputFile', type=argparse.FileType("rb"), help='Input File', required=True)
parser.add_argument('-o', '--output', dest='outputFile', type=argparse.FileType("wb"), help='Output File', required=True)
options = parser.parse_args()

if options.method == "hide":
    magicNumber = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52'
    try:
        hiddenContent = magicNumber + options.inputFile.read()
        options.outputFile.write(hiddenContent)
        options.outputFile.close()
        print("I added magic number in inputFile !")
        os.rename(options.outputFile.name, options.outputFile.name + ".png")
        print("I added '.png' in outputFile name !")
    except Exception as e:
        print(e)
else:
    try:        
        content = options.inputFile.read()[16:]
        options.outputFile.write(content)
        options.outputFile.close()
        print("I recovered the data from the inputFile ! ")

    except Exception as e:
        print(e)
