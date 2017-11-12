# -*- coding: utf-8 -*-

import collections


class ReplayToMap:

    def marshall(self, source):

        """
        Marshall the Replay into a map.

        Parameters
        ----------
        source : downloadbot_cache.models.Replay

        Returns
        -------
        typing.Mapping

        Raises
        ------
        None
        """

        marshalled = collections.OrderedDict()

        marshalled['replays_id'] = source.replays_id
        marshalled['replays_sid'] = source.replays_sid
        marshalled['name'] = source.name
        marshalled['created_at'] = source.created_at
        marshalled['created_by'] = source.created_by
        marshalled['updated_at'] = source.updated_at
        marshalled['updated_by'] = source.updated_by

        return marshalled

    def __repr__(self):
        repr_ = '{}()'
        return repr_.format(self.__class__.__name__)
