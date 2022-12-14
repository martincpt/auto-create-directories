import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from auto_create_directories import AutoCreateDirectories, auto_create_dirs, HOME_DIR, ROOT_DIR

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
        # with defaults
        auto_create_dirs_with_defaults = AutoCreateDirectories()
        self.assertFalse(bool(auto_create_dirs_with_defaults.dirs))

        # with args & create test dir upon creation
        auto_create_dirs_with_args = AutoCreateDirectories(dirs = [TEST_DIR], base_dir = self.current_file)
        self.assertTrue(TEST_DIR in auto_create_dirs_with_args.dirs)

    def test_set_base_dir(self) -> None:
        # test filepath as base dir
        auto_create_dirs_filepath = AutoCreateDirectories(base_dir = self.current_file)
        self.assertTrue(auto_create_dirs_filepath.base_dir in self.current_file)

        # test base dir literal: HOME
        auto_create_dirs_home = AutoCreateDirectories(base_dir = "HOME")
        self.assertEqual(auto_create_dirs_home.base_dir, HOME_DIR)

        # test base dir literal: ~
        auto_create_dirs_home_short = AutoCreateDirectories(base_dir = "~")
        self.assertEqual(auto_create_dirs_home_short.base_dir, HOME_DIR)

        # test base dir literal: ROOT
        auto_create_dirs_root = AutoCreateDirectories(base_dir = "ROOT")
        self.assertEqual(auto_create_dirs_root.base_dir, ROOT_DIR)

        # test with abs path directly
        auto_create_dirs_abs_path = AutoCreateDirectories(base_dir = self.current_dir)
        self.assertEqual(auto_create_dirs_abs_path.base_dir, self.current_dir)

        # test with invalid path
        invalid_path = "/probably/an/invalid/path/9685456321"
        with self.assertRaises(ValueError):
            AutoCreateDirectories(base_dir = invalid_path)

    def test_get(self) -> None:
        auto_create_dirs = AutoCreateDirectories(dirs = TEST_DIR, base_dir = self.current_file)
        test_dir_path = auto_create_dirs.get(TEST_DIR)
        self.assertEqual(test_dir_path, self.test_dir_path)

    def test_auto_create_dirs_shortcut(self) -> None:
        instance = auto_create_dirs()
        self.assertTrue(isinstance(instance, AutoCreateDirectories))

    def test_join_path(self) -> None:
        auto_create_dirs = AutoCreateDirectories()
        path_parts = ('simple', 'path', 'to', 'join')
        path_correct = 'simple/path/to/join'
        path = auto_create_dirs.join_path(*path_parts)
        self.assertEqual(str(path), path_correct)

    def test_is_file(self) -> None:
        path = self.current_file
        self.assertTrue(AutoCreateDirectories.is_file(path))

    def test_is_dir(self) -> None:
        path = self.current_dir
        self.assertTrue(AutoCreateDirectories.is_dir(path))

    def test_extra_get_root_dir_when_sub_created(self) -> None:
        sub_dir = os.path.join(TEST_DIR, 'subdir')
        sub_dir_abs_path = os.path.join(self.test_dir_path, 'subdir')
        sub_dir_root = os.path.dirname(sub_dir_abs_path)
        auto_create_dirs = AutoCreateDirectories(dirs = [sub_dir], base_dir = self.current_file)
        result = auto_create_dirs.get(TEST_DIR)
        self.assertEqual(result, sub_dir_root)
        # clean up
        os.rmdir(sub_dir_abs_path)
        


if __name__ == '__main__':
    unittest.main()