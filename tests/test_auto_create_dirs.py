import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from auto_create_directories import AutoCreateDirectories, auto_create_dirs

TEST_DIR: str = "_test"

class AutoCreateDirectories_TestCase(unittest.TestCase):
    current_file: str = __file__
    current_dir: str = os.path.dirname(current_file)
    parent_dir: str = os.path.dirname(current_dir)
    test_dir_path: str = os.path.join(current_dir, TEST_DIR)

    @classmethod
    def tearDownClass(cls) -> None:
        # remove created test dir
        os.rmdir(cls.test_dir_path)

    def test_init(self) -> None:
        auto_create_dirs_with_defaults = AutoCreateDirectories()
        self.assertFalse(bool(auto_create_dirs_with_defaults.dirs))

        auto_create_dirs_with_args = AutoCreateDirectories(dirs = [TEST_DIR], relative_file = __file__)
        self.assertTrue(TEST_DIR in auto_create_dirs_with_args.dirs)

    def test_set_base_dir(self) -> None:
        # test base dir literals: current
        auto_create_dirs_current = AutoCreateDirectories(base_dir = "CURRENT_DIRECTORY", relative_file = self.current_file)
        self.assertEqual(auto_create_dirs_current.base_dir, self.current_dir)

        # test base dir literals: parent
        auto_create_dirs_parent = AutoCreateDirectories(base_dir = "PARENT_DIRECTORY", relative_file = self.current_file)
        self.assertEqual(auto_create_dirs_parent.base_dir, self.parent_dir)

        # test with abs path directly
        auto_create_dirs_abs_path = AutoCreateDirectories(base_dir = self.current_dir)
        self.assertEqual(auto_create_dirs_abs_path.base_dir, self.current_dir)

        # test with invalid path
        invalid_path = "probably/an/invalid/path/9685456321"
        with self.assertRaises(ValueError):
            AutoCreateDirectories(base_dir = invalid_path)

    def test_get_path(self) -> None:
        auto_create_dirs = AutoCreateDirectories()
        path_parts = ['simple', 'path', 'to', 'join']
        path_correct = 'simple/path/to/join'
        path = auto_create_dirs.get_path(*path_parts)
        self.assertEqual(str(path), path_correct)

    def test_get(self) -> None:
        auto_create_dirs = AutoCreateDirectories(dirs = TEST_DIR, relative_file = __file__)
        test_dir_path = auto_create_dirs.get(TEST_DIR)
        self.assertEqual(test_dir_path, self.test_dir_path)

    def test_auto_create_dirs_shortcut(self) -> None:
        instance = auto_create_dirs()
        self.assertTrue(isinstance(instance, AutoCreateDirectories))


if __name__ == '__main__':
    unittest.main()