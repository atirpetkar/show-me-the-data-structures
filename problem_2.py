import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # List to store all matched paths
    match_path_list = list()

    def find_files_recursive(path):
        path_list = os.scandir(path)

        # Process each file/folder under each path
        for dir_entry in path_list:
            # For file, match suffix and add to list
            if dir_entry.is_file():
                if dir_entry.path.endswith(suffix):
                    match_path_list.append(dir_entry.path)
                continue

            # For sub-directories, call the function recursively for processing
            if dir_entry.is_dir():
                find_files_recursive(dir_entry.path)

    find_files_recursive(path)

    return match_path_list


def test_function(test_case):
    output = find_files(test_case[0], test_case[1])
    expected_output = test_case[2]
    print(output)
    if sorted(output) == sorted(expected_output):
        print("Pass")
    else:
        print("Fail")


test_case_1 = ['.c', './testdir', ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']]
test_function(test_case_1)
# Should output: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
