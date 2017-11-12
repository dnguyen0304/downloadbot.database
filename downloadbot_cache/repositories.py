# -*- coding: utf-8 -*-

import abc


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
