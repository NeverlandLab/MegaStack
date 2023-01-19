import logging

from MegaStack.core_settings.base_settings import DEBUG


class TestClass:
    def test_echo_debug(self):
        logging.info(DEBUG)
