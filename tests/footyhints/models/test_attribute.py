from web.models import Attribute

from tests.footyhints.unit_test import UnitTest


class TestAttributeModel(UnitTest):
    def test_init(self):
        attribute = Attribute(
            name='Test Name',
            value='100',
            description='Test description',
            game=self.game
        )
        assert attribute.name == 'Test Name'
        assert attribute.value == '100'
        assert attribute.description == 'Test description'
        assert attribute.game == self.game

    def test_save(self):
        attribute = Attribute(
            name='Test Name',
            value='100',
            description='Test description',
            game=self.game
        )
        assert attribute.id is None
        attribute.save()
        assert attribute.id is not None
