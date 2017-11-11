# -*- coding: utf-8 -*-

import abc


class Model(metaclass=abc.ABCMeta):
    pass


class Base(Model):

    def __init__(self,
                 created_at=None,
                 created_by=0,
                 updated_at=None,
                 updated_by=0):

        """
        Parameters
        ----------
        created_at : datetime.datetime
            When the entity was originally created. Defaults to None.
        created_by : int
            Who originally created the entity. Defaults to 0.
        updated_at : datetime.datetime
            When the entity was last updated. Defaults to None.
        updated_by : int
            Who last updated the entity. Defaults to 0.
        """

        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by


class Replay(Base):

    def __init__(self, name, replays_id=0, replays_sid=""):

        """
        Replay model.

        Parameters
        ----------
        name : str
        replays_id : int
            Private unique identifier. This field should not be used
            externally. Defaults to 0.
        replays_sid : str
            Unique identifier. Defaults to "".
        """

        super().__init__()
        self.replays_id = replays_id
        self.replays_sid = replays_sid
        self.name = name

    def __repr__(self):
        repr_ = '<{}(replays_id={}, replays_sid="{}", name="{}")>'
        return repr_.format(self.__class__.__name__,
                            self.replays_id,
                            self.replays_sid,
                            self.name)
