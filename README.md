# Auto Create Directories (for python)

![Requirement: Python >= 3.10](https://img.shields.io/badge/Python-%3E%3D%203.10-blue)

A simple python utility to automatically create and manage required directories. 

For example, you may have folders with dynamically created contents, or larger directories that not necessarily part of your package but when you run your code, you have to make sure they exist.

## Installation
```
pip install git+https://github.com/martincpt/auto-create-directories.git
```

## Typical Usage / Quickstart

Assuming you need the following folder structure in your project. 
```
module/
├── main.py
├── datasets/   <not exists>
└── results/    <not exists>
    └── models/ <not exists>
```

```python
# in your main.py
from auto_create_directories import AutoCreateDirectories

auto_create_dirs = AutoCreateDirectories(["datasets", "results/models"], __file__)

# if you need the absolute path of one of them
datasets_path = auto_create_dirs.get("datasets")
results_path = auto_create_dirs.get("results")
models_path = auto_create_dirs.get("results/models")
```

## It's safe
Even if they already exist, it's safe to call repetitively. It won't override your existing directories.

## More examples
```python 
from auto_create_directories import AutoCreateDirectories

# directories can be created during initialization but not required
auto_create_dirs = AutoCreateDirectories()
auto_create_dirs_single = AutoCreateDirectories("single_dir")
auto_create_dirs_multiply = AutoCreateDirectories(["multiply", "directories"])

# and they also can be created later on
auto_create_dirs.create("new_dir")
auto_create_dirs.create("another_dir/even_with_child")

# AutoCreateDirectories.get also creates the directory if it doesn't exist
# and returns with the absolute path (.get and .create are aliases)
another_dir = auto_create_dirs.get("another_dir")

# by default, directories will be created in the current user's home folder
# this can be changed by specifying the base_dir argument
auto_create_dirs = AutoCreateDirectories(base_dir = "/path/to/my/awesome/module")

# you can pass a filepath too, then its parent directory will be used
auto_create_dirs = AutoCreateDirectories(base_dir = "/even/filepath/works/but_its_parent_will_be_used.py")

# in most cases, you probably want to create directories relative to your current file
# this can be really simple by passing the __file__ variable
auto_create_dirs = AutoCreateDirectories(base_dir = __file__)
```

## Note
For safety reasons this library **is not capable to remove directories**. It is meant for quickly setup and create required folder structures in your modules.
