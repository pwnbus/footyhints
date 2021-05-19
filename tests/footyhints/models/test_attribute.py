from web.models import Attribute

from tests.footyhints.unit_test import UnitTest


class TestAttributeModel(UnitTest):
    def setup(self):
        super().setup()
        self.attribute = Attribute(
            name='Test Name',
            value='100',
            description='Test description',
            game=self.game
        )

    def test_init(self):
        assert self.attribute.name == 'Test Name'
        assert self.attribute.value == '100'
        assert self.attribute.description == 'Test description'
        assert self.attribute.game == self.game

    def test_save(self):
        assert self.attribute.id is None
        self.attribute.save()
        assert self.attribute.id is not None
