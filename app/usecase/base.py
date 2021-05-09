from abc import ABCMeta, abstractmethod


class BaseHandler(ABCMeta):
    @abstractmethod
    def call(self):
        """
        call
        """
        pass
