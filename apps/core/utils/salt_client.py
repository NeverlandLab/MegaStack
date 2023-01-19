import requests

from MegaStack.core_settings.salt_settings import SALT_REST_URL, SALT_USER, SALT_PASSWORD


class SaltClient:
    def __init__(self):
        self.url = SALT_REST_URL + '/run'
        self.jobs_url = SALT_REST_URL + '/jobs/'
        self.headers = {'Accept': 'application/json'}
        self.data = {
            'username': SALT_USER,
            'password': SALT_PASSWORD,
            'eauth': 'pam',
        }

    def exec(self, exec_data, client='local'):
        """
        执行Salt指令
        :param client:  可选 local、local_async、wheel、ssh、runner
        :return:
        """
        request_data = {
            **self.data,
            'client': client,
            **exec_data
        }
        req = requests.post(self.url, headers=self.headers,
                            json=request_data, verify=False)
        return req.json()['return']

    def load_async_job_result(self, jid):
        """
        加载作业信息
        :return:
        """
        request_data = {
            **self.data,
            'client': 'runner',
            'fun': 'jobs.lookup_jid',
            'jid': jid
        }
        req = requests.post(self.url, headers=self.headers,
                            json=request_data, verify=False)
        return req.json()['return']
