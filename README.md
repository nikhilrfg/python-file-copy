
# Python File Copy Program

## Description
This Python program copies data from a source file to a destination file using binary file operations and a buffer.

## Features
- Reads a source file in binary mode (`rb`)
- Creates a destination file in binary write mode (`wb`)
- Uses a 64 KiB buffer
- Copies data in chunks
- Counts the number of bytes written
- Handles file opening and copying errors

## Requirements
- Python 3

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

   python file_copy.py

4. Enter the source file name.
5. Enter the destination file name.

## Example
Enter the source file name: sample.txt
Enter the destination file name: sample_copy.txt

The program displays the number of bytes copied.

## Important Functions
- open(): Opens a file.
- readinto(): Reads bytes into a buffer.
- write(): Writes bytes to a file.
- bytearray(): Creates a mutable byte buffer.
- strerror(): Converts an OS error number into a readable message.
- close(): Closes an open file.

## Testing
- Copy an existing file.
- Attempt to copy a missing file.
- Copy an empty file.
- Copy a large file.

## Note
The destination file will be overwritten if it already exists.
