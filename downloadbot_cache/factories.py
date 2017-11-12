# -*- coding: utf-8 -*-

import logging
import logging.config

import redis

from . import handlers
from . import marshallers
from . import parsers
from . import repositories


class Logger:

    def __init__(self, properties):

        """
        Parameters
        ----------
        properties : typing.Mapping
        """

        self._properties = properties

    def create(self):

        """
        Returns
        -------
        logging.Logger

        Raises
        ------
        KeyError
            If an environment or property variable could not be found.
        """

        # Set the global configuration options.
        logging.config.dictConfig(config=self._properties['logging'])

        # Create the logger.
        logger = logging.getLogger(name=self._properties['logger']['name'])

        return logger

    def __repr__(self):
        repr_ = '{}(properties={})'
        return repr_.format(self.__class__.__name__, self._properties)


class EventHandler:

    def __init__(self, properties):

        """
        Parameters
        ----------
        properties : typing.Mapping
        """

        self._properties = properties

    def create(self):

        """
        Returns
        -------
        downloadbot_cache.handlers.Event

        Raises
        ------
        KeyError
            If an environment or property variable could not be found.
        """

        # Create the logger.
        logger_factory = Logger(properties=self._properties)
        logger = logger_factory.create()

        # Create the event parser.
        event_parser = parsers.S3ObjectCreatedEvent()

        # Create the client.
        client = redis.StrictRedis(host=self._properties['cache']['hostname'],
                                   port=self._properties['cache']['port'])

        # Create the marshaller.
        marshaller = marshallers.ReplayToLinkedHash()

        # Create the repository.
        repository = repositories.Redis(client=client, marshaller=marshaller)

        # Include default values for SID fields.
        repository = repositories.SidDefaulting(repository=repository)

        # Include default values for metadata fields.
        repository = repositories.MetadataDefaulting(repository=repository)

        # Include logging.
        repository = repositories.Logging(repository=repository, logger=logger)

        # Create the event handler.
        event_handler = handlers.Persistence(event_parser=event_parser,
                                             repository=repository)
        # Include logging.
        event_handler = handlers.Logging(event_handler=event_handler,
                                         logger=logger)
        return event_handler

    def __repr__(self):
        repr_ = '{}(properties={})'
        return repr_.format(self.__class__.__name__, self._properties)
