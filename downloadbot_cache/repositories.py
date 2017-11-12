# -*- coding: utf-8 -*-

import abc
import datetime
import random
import string

import redis
from downloadbot_common import utility

_TIME_ZONE_NAME = 'UTC'
_SID_LENGTH = 32
_SID_CHARACTERS = string.ascii_letters + string.digits


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add(self, model):

        """
        Queue the model to be synchronized.

        Parameters
        ----------
        model : downloadbot_cache.models.Model

        Returns
        -------
        None

        Raises
        ------
        None
        """

        raise NotImplementedError


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


def _generate_sid(characters=_SID_CHARACTERS, length=_SID_LENGTH):

    sid = ''.join(random.SystemRandom().choice(characters)
                  for _
                  in range(length))
    return sid


def _set_sid(model, sid):

    result = filter(lambda x: not x.startswith('_') and x.endswith('_sid'),
                    dir(model))
    try:
        attribute = next(result)
    except StopIteration:
        template = 'An SID attribute was not found on the model {}.'
        raise AttributeError(template.format(model))

    setattr(model, attribute, sid)


def _set_metadata(entity, by, _time_zone_name=_TIME_ZONE_NAME):

    time_zone = utility.TimeZone.from_name(_time_zone_name)
    timestamp = datetime.datetime.utcnow().replace(tzinfo=time_zone)

    if not entity.created_at and not entity.created_by:
        entity.created_at = timestamp
        entity.created_by = by
    else:
        entity.updated_at = timestamp
        entity.updated_by = by
