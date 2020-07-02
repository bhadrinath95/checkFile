# Check File

This project will check for files within the given directory and its child directories and write to .csv file.

## Setup

Use the package manager pip to install ConfigParser

```bash
pip install ConfigParser --user
```

## Configuration

You can configure which directory for searching files.

```properties
[ConfigurationSection]
directory.path=D:\Workspace

[ResultantSection]
output.path=D:\Workspace\PythonWorkspace\PythonTraining\OutputFolder
output.filename=output.csv
```

## Usage

```python
listOfFile = os.listdir(dirName)
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            checkForFile(fullPath, outputfile)
        else:
            extension = os.path.splitext(entry)[1]
```
