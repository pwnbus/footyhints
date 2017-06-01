from footyhints.models.attribute import Attribute

from tests.footyhints.unit_test import UnitTest


class TestAttributeInit(UnitTest):
    def test_init(self):
        attribute = Attribute(name='Test Name', value='100', description='Test description', game=self.game)
        assert attribute.name == 'Test Name'
        assert attribute.value == '100'
        assert attribute.description == 'Test description'
        assert attribute.game == self.game


class TestAttributeSave(UnitTest):
    def test_basic_save(self):
        attribute = Attribute(name='Test Name', value='100', description='Test description')
        assert attribute.id is None
        self.session.add(attribute)
        self.session.commit()
        assert attribute.id is not None
