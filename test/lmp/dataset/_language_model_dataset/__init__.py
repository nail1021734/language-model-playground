r"""Test `lmp.dataset._language_model_dataset.py`.

Usage:
    python -m unittest test.lmp.dataset.LanguageModelDataset.__init__
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import inspect
import unittest


class TestLanguageModelDataset(unittest.TestCase):
    r"""Test case for `lmp.dataset._langeage_model_dataset.py`."""

    def test_signature(self):
        r"""Ensure signature consistency."""
        msg = 'Inconsistent module signature.'

        try:
            # pylint: disable=C0415
            import lmp
            import lmp.dataset
            import lmp.dataset._language_model_dataset
            # pylint: enable=C0415

            # pylint: disable=W0212
            self.assertTrue(
                inspect.ismodule(lmp.dataset._language_model_dataset),
                msg=msg
            )
            # pylint: enable=W0212
        except ImportError:
            self.fail(msg=msg)

    def test_module_attributes(self):
        r"""Declare required module attributes."""
        msg1 = 'Missing module attribute `{}`.'
        msg2 = 'Module attribute `{}` must be a class.'
        msg3 = 'Inconsistent module signature.'
        examples = ('LanguageModelDataset',)

        try:
            # pylint: disable=C0415
            # pylint: disable=W0212
            import lmp
            import lmp.dataset
            import lmp.dataset._language_model_dataset

            for attr in examples:
                self.assertTrue(
                    hasattr(lmp.dataset._language_model_dataset, attr),
                    msg=msg1.format(attr)
                )
                self.assertTrue(
                    inspect.isclass(getattr(
                        lmp.dataset._language_model_dataset,
                        attr
                    )),
                    msg=msg2.format(attr)
                )
            # pylint: enable=W0212
            # pylint: enable=C0415
        except ImportError:
            self.fail(msg=msg3)


if __name__ == '__main__':
    unittest.main()
