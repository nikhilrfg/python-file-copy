
from os import strerror

# Lines 3-8:
# Ask the user for the name of the source file to copy.
# Try to open the file in binary read mode ('rb').
# If opening the file fails, display an error message and stop execution.
# The exit() function stops the program and passes a completion code to the OS.
# A completion code of 0 indicates success; a non-zero code indicates a problem.
# The errno value identifies the nature of the error.

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)


# Lines 10-16:
# Ask the user for the destination file name.
# Try to open the destination file in binary write mode ('wb').
# If the file does not exist, Python creates it.
# If it already exists, its existing contents will be overwritten.
# If creating the destination file fails, display an error,
# close the source file, and stop execution.

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)


# Line 18:
# Prepare a memory area for transferring data from the source file
# to the destination file. This memory area is called a buffer.
# The buffer size is 65,536 bytes, or 64 KiB.
# A larger buffer can reduce the number of input/output operations,
# but increasing its size does not always improve performance.

buffer = bytearray(65536)

# Line 19:
# Initialize a counter to track the total number of bytes copied.

total = 0

try:
    # Line 21:
    # Read the first chunk of data from the source file into the buffer.
    # readinto() returns the number of bytes actually read.

    readin = src.readinto(buffer)

    # Line 22:
    # Continue copying while the number of bytes read is greater than 0.
    # A return value of 0 indicates the end of the file.

    while readin > 0:
        print("Bytes read:", readin)

        # Line 23:
        # Write the bytes read from the buffer to the destination file.
        # buffer[:readin] selects only the valid bytes that were read.
        # write() returns the number of bytes written.

        written = dst.write(buffer[:readin])

        # Line 24:
        # Add the number of bytes written to the total counter.

        total += written
        print("Total bytes written:", total)

        # Line 25:
        # Read the next chunk of data from the source file.

        readin = src.readinto(buffer)

except IOError as e:
    # Display an error if a problem occurs during copying.
    print("Cannot copy the file: ", strerror(e.errno))
    exit(e.errno)


# Final lines:
# Display the total number of bytes successfully written.
# Close both files to release system resources.
# The copying operation is now complete.

print(total, 'byte(s) successfully written')
src.close()
dst.close()
