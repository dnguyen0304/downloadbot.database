# -*- coding: utf-8 -*-

from downloadbot_common import utility

from downloadbot_database import factories


def lambda_handler(event, context):

    """
    Handle the event.

    Parameters
    ----------
    event : typing.Mapping
    context : typing.Mapping

    Returns
    -------
    None

    Raises
    ------
    None
    """

    properties = utility.get_configuration()
    event_handler = factories.EventHandler(properties=properties).create()

    event_handler.handle(event=event)
