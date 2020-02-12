# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.8.1 Python SDK

    Pure Storage FlashBlade REST 1.8.1 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.8.1
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Blade(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'details': 'str',
        'progress': 'float',
        'raw_capacity': 'int',
        'status': 'str',
        'target': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'details': 'details',
        'progress': 'progress',
        'raw_capacity': 'raw_capacity',
        'status': 'status',
        'target': 'target'
    }

    def __init__(self, id=None, name=None, details=None, progress=None, raw_capacity=None, status=None, target=None):
        """
        Blade - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._details = None
        self._progress = None
        self._raw_capacity = None
        self._status = None
        self._target = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if details is not None:
          self.details = details
        if progress is not None:
          self.progress = progress
        if raw_capacity is not None:
          self.raw_capacity = raw_capacity
        if status is not None:
          self.status = status
        if target is not None:
          self.target = target

    @property
    def id(self):
        """
        Gets the id of this Blade.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this Blade.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Blade.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this Blade.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Blade.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this Blade.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Blade.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this Blade.
        :type: str
        """

        self._name = name

    @property
    def details(self):
        """
        Gets the details of this Blade.
        The details of the blade's status.

        :return: The details of this Blade.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Blade.
        The details of the blade's status.

        :param details: The details of this Blade.
        :type: str
        """

        self._details = details

    @property
    def progress(self):
        """
        Gets the progress of this Blade.
        The progress of an ongoing evacuation, if the blade is being evacuated.

        :return: The progress of this Blade.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this Blade.
        The progress of an ongoing evacuation, if the blade is being evacuated.

        :param progress: The progress of this Blade.
        :type: float
        """

        self._progress = progress

    @property
    def raw_capacity(self):
        """
        Gets the raw_capacity of this Blade.
        The blade's capacity in bytes.

        :return: The raw_capacity of this Blade.
        :rtype: int
        """
        return self._raw_capacity

    @raw_capacity.setter
    def raw_capacity(self, raw_capacity):
        """
        Sets the raw_capacity of this Blade.
        The blade's capacity in bytes.

        :param raw_capacity: The raw_capacity of this Blade.
        :type: int
        """

        self._raw_capacity = raw_capacity

    @property
    def status(self):
        """
        Gets the status of this Blade.
        The blade's current status.

        :return: The status of this Blade.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Blade.
        The blade's current status.

        :param status: The status of this Blade.
        :type: str
        """

        self._status = status

    @property
    def target(self):
        """
        Gets the target of this Blade.
        The evacuation target.

        :return: The target of this Blade.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this Blade.
        The evacuation target.

        :param target: The target of this Blade.
        :type: str
        """

        self._target = target

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Blade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other