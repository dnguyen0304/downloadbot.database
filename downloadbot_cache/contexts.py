# -*- coding: utf-8 -*-

import datetime

from downloadbot_common import messaging

from . import topics




class SidDefaulting(Context):

    def __init__(self,
                 db_context,
                 _generate_sid=_generate_sid,
                 _set_sid=_set_sid):

        """
        Component to include default values for SID fields.

        Parameters
        ----------
        db_context : downloadbot_cache.contexts.Context
        """

        self._db_context = db_context
        self._generate_sid = _generate_sid
        self._set_sid = _set_sid

    def add(self, model):
        try:
            # This is a leaky abstraction.
            entity_state = sqlalchemy.inspect(model)
        except sqlalchemy.exc.NoInspectionAvailable:
            pass
        else:
            if entity_state.transient:
                sid = self._generate_sid()
                try:
                    self._set_sid(model=model, sid=sid)
                except AttributeError:
                    pass
        self._db_context.add(model=model)

    def commit(self):
        self._db_context.commit()

    def __repr__(self):
        repr_ = '<{}(db_context={})>'
        return repr_.format(self.__class__.__name__, self._db_context)


def _set_metadata(entity, entity_state, by):

    # Should these timestamps instead be time zone-aware?
    if entity_state.transient:
        entity.created_at = datetime.datetime.utcnow()
        entity.created_by = by
    elif entity_state.persistent:
        entity.updated_at = datetime.datetime.utcnow()
        entity.updated_by = by


class MetadataDefaulting(Context):

    _BY = -1

    def __init__(self, db_context, _set_metadata=_set_metadata):

        """
        Component to include default values for metadata fields.

        Parameters
        ----------
        db_context : downloadbot_cache.contexts.Context
        """

        self._db_context = db_context
        self._set_metadata = _set_metadata

    def add(self, model):
        try:
            # This is a leaky abstraction.
            entity_state = sqlalchemy.inspect(model)
        except sqlalchemy.exc.NoInspectionAvailable:
            pass
        else:
            self._set_metadata(entity=model,
                               entity_state=entity_state,
                               by=self._BY)
        self._db_context.add(model=model)

    def commit(self):
        self._db_context.commit()

    def __repr__(self):
        repr_ = '<{}(db_context={})>'
        return repr_.format(self.__class__.__name__, self._db_context)


class Logging(Context):

    def __init__(self, db_context, logger):

        """
        Component to include logging.

        Parameters
        ----------
        db_context : downloadbot_cache.contexts.Context
        logger : logging.Logger
        """

        self._db_context = db_context
        self._logger = logger

        # This follows last write wins semantics.
        self._last_added_model = None

    def add(self, model):
        self._db_context.add(model=model)
        self._last_added_model = model

    def commit(self):
        self._db_context.commit()
        event = messaging.events.Structured(topic=topics.Topic.ENTITY_ADDED,
                                            arguments=dict())
        self._logger.info(msg=event.to_json())

    def __repr__(self):
        repr_ = '<{}(db_context={}, logger={})>'
        return repr_.format(self.__class__.__name__,
                            self._db_context,
                            self._logger)
