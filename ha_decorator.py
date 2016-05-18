# -*- coding: utf-8 -*-
import logging
import threading
from kazoo.client import KazooClient

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-8s %(message)s"
)


class HaDecorator(object):
    ELECTION_PATH = "/ha-zookeeper/election"

    def __init__(self, hosts):
        self.hosts = hosts
        self.zk = None

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            self.zk = KazooClient(hosts=self.hosts)
            self.zk.start()
            election = self.zk.Election(self.ELECTION_PATH)
            election.run(lambda: f(*args, **kwargs))

        return wrapped

    def __del__(self):
        if self.zk != None:
            self.zk.stop()
