# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.11 Python SDK

    Pure Storage FlashBlade REST 1.11 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.11
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ObjectStoreUser(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

#BEGIN_CUSTOM
    # IR-51527: Prevent Pytest from attempting to collect this class based on name.
    __test__ = False
#END_CUSTOM

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'created': 'int',
        'id': 'str',
        'account': 'Reference',
        'access_keys': 'list[FixedReferenceWithId]'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'id': 'id',
        'account': 'account',
        'access_keys': 'access_keys'
    }

    def __init__(self, name=None, created=None, id=None, account=None, access_keys=None):  # noqa: E501
        """ObjectStoreUser - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._created = None
        self._id = None
        self._account = None
        self._access_keys = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if access_keys is not None:
            self.access_keys = access_keys

    @property
    def name(self):
        """Gets the name of this ObjectStoreUser.  # noqa: E501

        The name of the object (e.g., a file system or snapshot).  # noqa: E501

        :return: The name of this ObjectStoreUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectStoreUser.

        The name of the object (e.g., a file system or snapshot).  # noqa: E501

        :param name: The name of this ObjectStoreUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """Gets the created of this ObjectStoreUser.  # noqa: E501

        Creation timestamp of the object  # noqa: E501

        :return: The created of this ObjectStoreUser.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ObjectStoreUser.

        Creation timestamp of the object  # noqa: E501

        :param created: The created of this ObjectStoreUser.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this ObjectStoreUser.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this ObjectStoreUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectStoreUser.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this ObjectStoreUser.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account(self):
        """Gets the account of this ObjectStoreUser.  # noqa: E501

        Reference to the associated account.  # noqa: E501

        :return: The account of this ObjectStoreUser.  # noqa: E501
        :rtype: Reference
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ObjectStoreUser.

        Reference to the associated account.  # noqa: E501

        :param account: The account of this ObjectStoreUser.  # noqa: E501
        :type: Reference
        """

        self._account = account

    @property
    def access_keys(self):
        """Gets the access_keys of this ObjectStoreUser.  # noqa: E501

        References to the user's access keys.  # noqa: E501

        :return: The access_keys of this ObjectStoreUser.  # noqa: E501
        :rtype: list[FixedReferenceWithId]
        """
        return self._access_keys

    @access_keys.setter
    def access_keys(self, access_keys):
        """Sets the access_keys of this ObjectStoreUser.

        References to the user's access keys.  # noqa: E501

        :param access_keys: The access_keys of this ObjectStoreUser.  # noqa: E501
        :type: list[FixedReferenceWithId]
        """

        self._access_keys = access_keys

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ObjectStoreUser, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ObjectStoreUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other