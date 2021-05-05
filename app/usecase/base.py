from abc import ABCMeta, abstractmethod


class BaseHandler():
    @abstractmethod
    def call(self):
        """
        call
        """
        pass
