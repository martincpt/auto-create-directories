from genericpath import isfile
import os

from typing import Literal, Any

HOME_DIR = os.path.expanduser("~")
ROOT_DIR = os.path.abspath(os.sep)

BaseDirLiterals = Literal["~", "HOME", "ROOT"]

class AutoCreateDirectories:
    """Utility class to automatically create directories in a given directory.

    Args:
        dirs (list[str] | str, optional): The list of (or single) directory name(s) to create. Defaults to [].
        base_dir (str | BaseDirLiterals, optional): An absolute path to be used as base directory or one of the BaseDirLiterals. Defaults to "HOME_DIR".
    """ 

    def __init__(self, dirs: list[str]|str  = [], base_dir: str|BaseDirLiterals = HOME_DIR) -> None:             
        # make dirs iterable
        dirs = dirs if isinstance(dirs, list) else [dirs]

        # dirs dictionary will hold created directories
        self.dirs = {}

        # set base dir
        self.set_base_dir(base_dir)
         
        # auto create the given directories
        for dir in dirs:
            self.create(dir)        

    def set_base_dir(self, base_dir: str|BaseDirLiterals) -> None:
        """Sets the base directory according to the relative file.

        Args:
            base_dir (str|BaseDirLiterals): An absolute path to be used as base directory or one of the BaseDirLiterals.

        Raises:
            ValueError: If invalid base_dir value was given.
        """

        # if filepath passed
        if self.is_file(base_dir):
            # use its parent directory
            self.base_dir = os.path.dirname(os.path.abspath(base_dir))
            return
        # handle special literals
        if base_dir in ["HOME", "~"]:
            # set home folder as the base
            self.base_dir = HOME_DIR
            return
        if base_dir == "ROOT":
            # set drive's root as the base
            self.base_dir = ROOT_DIR
            return
        
        # any other case: handle as absolute path
        if os.path.exists(base_dir):
            # set abs path
            self.base_dir = base_dir
        else:
            # but it must exists
            raise ValueError("`base_dir` should be either an absolute path which already exists or one of the BaseDirLiterals.")

    def create(self, dir: str) -> str:
        """Gets or creates the given directory. 

        Args:
            dir (str): The name of the directory to create.

        Returns:
            str: The absolute path of the directory.
        """
        return self.get(dir)

    def get(self, dir: str) -> str:
        """Gets or creates the given directory. 

        Args:
            dir (str): The name of the directory to get or create.

        Returns:
            str: The absolute path of the directory.
        """

        # early return if current instance already holds it
        if dir in self.dirs:
            return self.dirs[dir]

        # get the abs path
        dir_abs_path = dir if os.path.isabs(dir) else os.path.join(self.base_dir, dir)

        # check if exists and create if it doesn't
        if not os.path.exists(dir_abs_path):
            os.makedirs(dir_abs_path)   

        # store the path to dirs dictionary
        self.dirs[dir] = dir_abs_path

        return dir_abs_path

    @classmethod
    def join_path(cls, *args: list[str]) -> str:
        """A shortcut for os.path.join()"""
        return os.path.join(*args)

    @classmethod
    def is_file(cls, path: str) -> bool:
        """A shortcut for os.path.isfile()"""
        return os.path.isfile(path)

    @classmethod
    def is_dir(cls, path: str) -> bool:
        """A shortcut for os.path.isdir()"""
        return os.path.isdir(path)


def auto_create_dirs(*args, **kwargs) -> AutoCreateDirectories:
    """Generic shortcut for creating an AutoCreateDirectories instance on the fly in case a snake cased callable better fits the code style.

    Returns:
        AutoCreateDirectories: The created AutoCreateDirectories instance.
    """
    return AutoCreateDirectories(*args, **kwargs)
