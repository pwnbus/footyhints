import re

from footyhints.version import version


class TestVersion(object):

    def test_version_format(self):
        # 'number.number.number'
        pattern = re.compile("^([0-9]+).([0-9]+).([0-9]+)$")
        assert pattern.match(version)
