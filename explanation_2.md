# Problem 2 - File Recursion - Explanation

For this solution, recursion technique was used so that for each entry encountered in a folder, will check whether it's a file or directory.

For file, the path (include the file name) will match with the suffix and append to list if match.

For directory, will call the function recursively with the directory path for further scanning and suffix matching.
