from unittest import TestCase

from gameyamlspiderandgenerator.util.fgi import template_dict
from yamlgenerator_hook_search import Search
from gameyamlspiderandgenerator.util.config import config

config.hook_configs ={'search': {'apple': ...,
                                 'google-play': ...}}
class Test(TestCase):
    def test_search(self):
        print(Search().setup({**template_dict, 'name': 'hollow knight', }))
        print(Search().setup({**template_dict, 'name': 'TUNIC', }))
        print(Search().setup({**template_dict, 'name': 'BLACKSAD : Under The Skin', }))
        print(Search().setup({**template_dict, 'name': 'A Glimpse Of Memory', }))
