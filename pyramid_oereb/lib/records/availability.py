# -*- coding: utf-8 -*-


class AvailabilityRecord(object):

    def __init__(self, fosnr, available=False):
        """
        The record to check if data is available for municipality.

        Args:
            fosnr (int): The unique id of the municipality.
            available (bool): Switch if data is available in municipality or not.
        """
        self.fosnr = fosnr
        self.available = available

    @classmethod
    def get_fields(cls):
        """
        Returns a list of available field names.

        Returns:
            listofstr: List of available field names.
        """
        return [
            'fosnr',
            'available'
        ]
