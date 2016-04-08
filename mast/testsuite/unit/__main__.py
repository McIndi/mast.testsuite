import os
import unittest

here = os.path.dirname(__file__)
suite = unittest.defaultTestLoader.discover(start_dir=here,
                                            top_level_dir=here)
unittest.TextTestRunner(verbosity=2).run(suite)
