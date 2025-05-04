## Introduction

This project provides a simple harness for working with the ODA File Converter and automating the process of converting DWG files to DXF format. It includes basic functionality for managing conversion settings and extracting information such as layer names from the resulting DXF files. The primary purpose of this tool is to serve as a starting point or a utility for integrating and extending the ODA File Converter within your own workflows.

This is not a full-fledged application, but a simple framework that allows easy interaction with the conversion process and access to the relevant data.

## Getting Started
1. Install ODA File Converter from [here](https://www.opendesign.com/guestfiles/oda_file_converter)

1. Install pip requirements 

``` bash
pip install -r requirements.txt
```

1. Run the app from the root directory
``` bash
python ./src/main.py
``` 

## Running The Tests
You can run the tests using pytest with the folowing command
```bash
pytest
```