import unittest
import os
from filesys import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.state_file = 'state.json'

    def test_mkdir(self):
        self.assertEqual(self.fs.mkdir('dir1'), 'dir1 created')
        # Fix
        self.assertEqual(self.fs.mkdir('dir1'), 'dir1 already exists')

    def test_cd(self):
        self.fs.mkdir('dir1')
        self.assertEqual(self.fs.cd('dir1'), None)
        self.assertEqual(self.fs.get_current_path(), '//dir1')
        self.assertEqual(self.fs.cd('nonexistent'), 'Invalid path')

    def test_ls(self):
        self.fs.mkdir('dir1')
        self.fs.mkdir('dir2')
        self.assertEqual(self.fs.ls(), ['dir1', 'dir2'])

    def test_touch(self):
        self.fs.touch('file1')
        self.assertEqual(self.fs.touch('file1'), 'File already exists')

    def test_echo(self):
        self.fs.touch('file1')
        self.assertEqual(self.fs.echo('Hello, World!', 'file1'), None)
        self.assertEqual(self.fs.echo('Hello, World!', 'nonexistent'), 'File not found')

    def test_cat(self):
        self.fs.touch('file1')
        self.fs.echo('Hello, World!', 'file1')
        self.assertEqual(self.fs.cat('file1'), 'Hello, World!')
        self.assertEqual(self.fs.cat('nonexistent'), 'File not found')

    def test_mv(self):
        self.fs.touch('file1')
        self.fs.mkdir('dir1')
        self.assertEqual(self.fs.mv('/file1', '/dir1'), None)
        self.fs.cd('dir1')
        self.assertEqual(self.fs.ls(), ['file1'])

    def test_cp(self):
        self.fs.touch('file1')
        self.fs.echo('Hello, World!', 'file1')
        self.fs.mkdir('dir1')
        self.assertEqual(self.fs.cp('/file1', '/dir1'), None)
        self.fs.cd('dir1')
        self.assertEqual(self.fs.cat('file1'), 'Hello, World!')

    def test_rm(self):
        self.fs.touch('file1')
        self.assertEqual(self.fs.rm('file1'), None)
        self.assertEqual(self.fs.rm('file1'), 'File or directory not found')
    
    def test_save_state(self):
        self.fs.save_state(self.state_file)
        self.assertTrue(os.path.exists(self.state_file))

    def test_load_state(self):
        self.fs.touch('testfile')
        self.fs.save_state(self.state_file)
        self.fs = FileSystem()
        self.fs.load_state(self.state_file)
        self.assertIn('testfile', self.fs.current.children)

    def tearDown(self):
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

if __name__ == '__main__':
    unittest.main()