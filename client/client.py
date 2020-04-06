"""
Author: kripanshu bhargava
topic and code reference/source: https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb
purpose: learning [Not for commercial use]
task: learn async calls and convert them to class and objects
"""
import asyncio
import signal
from typing import List

from api.api_handler import ApiHandler

api_handler = ApiHandler()


class Client:
    def __init__(self):
        signal.signal(signal.SIGINT, api_handler.signal_handler)

    def call_reddit(self, topic: List):
        for item in topic:
            return asyncio.ensure_future(api_handler.get_reddit_top(item))


    def complete_loop_now(self, future):
        api_handler.complete_loop(future)
