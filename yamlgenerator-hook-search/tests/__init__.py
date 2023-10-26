from unittest import TestCase

from gameyamlspiderandgenerator.util.fgi import template_dict
from gameyamlspiderandgenerator.util.spider import get_text
from yamlgenerator_hook_search import Search


class Test(TestCase):
    def test_search(self):
        print(Search().setup({**template_dict, 'name': 'hollow knight', }))
        print(Search().setup({**template_dict, 'name': 'TUNIC', }))
        print(Search().setup({**template_dict, 'name': 'BLACKSAD : Under The Skin', }))
