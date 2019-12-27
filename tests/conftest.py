from functools import partial
import textwrap

import pytest

TEST_TEMPLATE = """
def test_{sub}_1():
    assert True

def test_{sub}_2():
    assert '{sub}' == 'a'
"""

DOCS_TEMPLATE = """
Documentation for {sub}
=======================

::

    >>> a = 1
    >>> b = 2
    >>> a + b
    3
"""


@pytest.fixture
def testpackage(testdir):
    # Fixture to make a test package with a docs and code folder

    pkg = testdir.mkdir('testpackage')
    pkg.join('__init__.py').write('')
    for sub in ('a', 'b', 'c'):
        pkg.mkdir(sub).join('__init__.py').write('')
        pkg.join(sub).mkdir('tests').join('__init__.py').write('')
        pkg.join(sub).join('tests').join(f'test_{sub}.py').write(TEST_TEMPLATE.format(sub=sub))
    docs = testdir.mkdir('docs')
    for sub in ('a', 'c'):
        docs.mkdir(sub).join('index.rst').write(DOCS_TEMPLATE.format(sub=sub))
