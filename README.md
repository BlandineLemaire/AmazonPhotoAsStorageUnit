# AmazonPhotoAsStorageUnit:framed_picture::floppy_disk:
## Infos
This script is used to add the PNG magic number to the files you want to push to your amazon photo storage account

## How to use it 
```
usage: amazonbypass.py [-h] --method {hide,recover} -i <INPUTFILE> -o <OUTPUTFILE>

-h, --help                                            show this help message and exit
-m {hide,recover}, --method {hide,recover}            Select Method
-i INPUTFILE, --input INPUTFILE                       Input File
-o OUTPUTFILE, --output OUTPUTFILE                    Output File
```
## Notes:
:warning: Please add `.png` to your file to let Amazon accept it :warning:

Amazon does not seems to support files that are bigger than 48.82 Go

## TO-DO
- [x] Add png magic number
- [x] Remove png magic number
- [x] Automatically add `.png` when hiding
- [ ] Automatically remove `.png` when recovering
- [ ] push the file via API Requests
