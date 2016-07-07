from abc import ABCMeta, abstractmethod


class Serializer(object):
    """
    Generic serializer interface
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def serialize(self, obj):
        raise NotImplementedError

    def serialize_many(self, obj):
        return [self.serialize(o) for o in obj]
