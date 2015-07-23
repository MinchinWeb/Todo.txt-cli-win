import unittest
import todo


class Test_Setup(unittest.TestCase):

    def test_we_live(self):
        '''Test we should *always* pass'''
        pass

    def test_version(self):
        '''Version is available'''
        self.assertIsNotNone(todo.__version__)

    def test_load_base_modeule(self):
        '''Load testing base module'''
        import base
        # should run without any errors


def main():
    unittest.main()

if __name__ == '__main__':
    main()
