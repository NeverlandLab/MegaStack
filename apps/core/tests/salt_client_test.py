import logging

from apps.core.utils.salt_client import SaltClient


class TestClass:
    def test_sync_command(self):
        client = SaltClient()
        result = client.sync_command('*', 'test.ping')
        logging.info(result)

    def test_async_command(self):
        client = SaltClient()
        result = client.async_command('*', 'test.ping')
        logging.info(result)

    def test_load_async_job_result(self):
        client = SaltClient()
        result = client.load_async_job_result('20221231150940296415')
        logging.info(result)

    def test_get_minion_status(self):
        client = SaltClient()
        result = client.get_minion_status()
        logging.info(result)

    def test_list_minion_key_status(self):
        client = SaltClient()
        result = client.list_minion_key_status()
        logging.info(result)
