# Auto Create Directories
A simple utility to automatically create and manage required directories.

## Usage
```python 
from auto_create_directories import AutoCreateDirectories

# directories can be created during initialization but not required
auto_create_dirs = AutoCreateDirectories()
auto_create_dirs_single = AutoCreateDirectories("single_dir")
auto_create_dirs_multiply = AutoCreateDirectories(["multiply", "directories"])

# and they also can be created later on
new_dir_abs_path = auto_create_dirs.create("new_dir")

# AutoCreateDirectories.get also creates the directory if it doesn't exist
# and returns with the absolute path (.get and .create are aliases)
another_dir = auto_create_dirs.get("another_dir")

# by default, directories will be created in the current user's home folder
# this can be changed by specifying the base_dir argument
auto_create_dirs = AutoCreateDirectories(base_dir = "/path/to/my/awesome/module")

# you can pass a filepath too, then its parent directory will be used
auto_create_dirs = AutoCreateDirectories(base_dir = ""/even/filepath/works/but_its_parent_will_be_used.py")

# in most cases, you probably want to create directories relative to your current file
# this can be really simple by passing the __file__ variable
auto_create_dirs = AutoCreateDirectories(base_dir = __file__)
```

## Note
For safety reasons this library is not capable to remove directories. It is meant for quickly setup and create required folder structures of your modules.
