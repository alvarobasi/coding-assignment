# Coding assignment - Food database

In this repository can be found a solution to the food database coding assignment.

## Requirements

Just Python 3.7.9.

## Usage

In order to test it, the [test.py](https://github.com/alvarobasi/coding-assignment/blob/master/test.py) file should be executed with the following arguments:
- `-b`: Path to the graph_build.json file. 
- `-e`: Path to the graph_edits.json file
- `-ext`: Path to the img_extract.json file

Every parameter used in this program can also be tuned directly from the [config.py](https://github.com/alvarobasi/coding-assignment/blob/master/config.py) file.

```python
GRAPH_BUILD_PATH = "inputs/graph_build.json"
GRAPH_EDITS_PATH = "inputs/graph_edits.json"
IMG_EXTRACT_PATH = "inputs/img_extract.json"
```

## Results

The result dictionary containing the status of each image extract is printed at the end of the [test.py](https://github.com/alvarobasi/coding-assignment/blob/master/test.py) program. The results are also stored in a [result.json](https://github.com/alvarobasi/coding-assignment/blob/master/outputs/result.json). In order to evaluate the solution, this file is directly compared with the [expected_status.json](https://github.com/alvarobasi/coding-assignment/blob/master/inputs/expected_status.json) using the PyCharm compare tool, for example. Both files are identical.

## Credits

https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/GenTreeIntro.html
https://www.youtube.com/watch?v=4r_XR9fUPhQ&ab_channel=codebasics
