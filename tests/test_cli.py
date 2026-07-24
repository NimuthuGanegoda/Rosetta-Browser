import unittest

from rosetta_browser.main import ENGINE_REGISTRY, load_plugins


class TestRosettaBrowser(unittest.TestCase):
    def test_plugin_loading(self):
        # clear registry first just in case
        ENGINE_REGISTRY.clear()
        load_plugins()
        self.assertIn("Blink", ENGINE_REGISTRY)
        self.assertIn("Gecko", ENGINE_REGISTRY)

if __name__ == '__main__':
    unittest.main()
