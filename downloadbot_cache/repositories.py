# -*- coding: utf-8 -*-

import abc

import redis


class Replay(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add(self, model):

        """
        Queue the model to be synchronized.

        Parameters
        ----------
        model : downloadbot_cache.models.Replay

        Returns
        -------
        None

        Raises
        ------
        None
        """

        raise NotImplementedError


class Redis(Replay):

    def __init__(self, client, marshaller):

        """
        Implementation backed by the redis library.

        Parameters
        ----------
        client : redis.client.StrictRedis
        marshaller : downloadbot_cache.marshallers.ReplayToMap
        """

        self._client = client
        self._marshaller = marshaller

    def add(self, model):

        """
        The time complexity is O(n), where n is the number of fields
        being set.
        """

        # This should not use string literals.
        # This should catch redis.exceptions.ConnectionError and
        # redis.exceptions.TimeoutError exceptions. These exceptions
        # are not documented.

        # This operation is atomic.
        next_replay_id = self._client.incr('replays:id:next')
        model.replays_id = int(next_replay_id)
        mapping = self._marshaller.marshall(source=model)
        try:
            self._client.hmset('replays:' + next_replay_id, mapping=mapping)
        except redis.DataError:
            # An expected case has occurred. The map contains no items.
            pass

    def __repr__(self):
        repr_ = '{}(client={}, marshaller={})'
        return repr_.format(self.__class__.__name__,
                            self._client,
                            self._marshaller)
