# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.12 Python SDK

    Pure Storage FlashBlade REST 1.12 Python SDK. Compatible with REST API versions 1.0 - 1.12. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.12
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ActiveDirectory(object):
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
        'id': 'str',
        'name': 'str',
        'computer_name': 'str',
        'directory_servers': 'list[str]',
        'domain': 'str',
        'encryption_types': 'list[str]',
        'join_ou': 'str',
        'kerberos_servers': 'list[str]',
        'service_principal_names': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'computer_name': 'computer_name',
        'directory_servers': 'directory_servers',
        'domain': 'domain',
        'encryption_types': 'encryption_types',
        'join_ou': 'join_ou',
        'kerberos_servers': 'kerberos_servers',
        'service_principal_names': 'service_principal_names'
    }

    def __init__(self, id=None, name=None, computer_name=None, directory_servers=None, domain=None, encryption_types=None, join_ou=None, kerberos_servers=None, service_principal_names=None):  # noqa: E501
        """ActiveDirectory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._computer_name = None
        self._directory_servers = None
        self._domain = None
        self._encryption_types = None
        self._join_ou = None
        self._kerberos_servers = None
        self._service_principal_names = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if computer_name is not None:
            self.computer_name = computer_name
        if directory_servers is not None:
            self.directory_servers = directory_servers
        if domain is not None:
            self.domain = domain
        if encryption_types is not None:
            self.encryption_types = encryption_types
        if join_ou is not None:
            self.join_ou = join_ou
        if kerberos_servers is not None:
            self.kerberos_servers = kerberos_servers
        if service_principal_names is not None:
            self.service_principal_names = service_principal_names

    @property
    def id(self):
        """Gets the id of this ActiveDirectory.  # noqa: E501

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :return: The id of this ActiveDirectory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActiveDirectory.

        A non-modifiable, globally unique ID chosen by the system.  # noqa: E501

        :param id: The id of this ActiveDirectory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ActiveDirectory.  # noqa: E501

        The name of the object (e.g., a file system or snapshot).  # noqa: E501

        :return: The name of this ActiveDirectory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActiveDirectory.

        The name of the object (e.g., a file system or snapshot).  # noqa: E501

        :param name: The name of this ActiveDirectory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def computer_name(self):
        """Gets the computer_name of this ActiveDirectory.  # noqa: E501

        The common name of the computer account to be created in the Active Directory domain. If not specified, defaults to the name of the Active Directory configuration.  # noqa: E501

        :return: The computer_name of this ActiveDirectory.  # noqa: E501
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this ActiveDirectory.

        The common name of the computer account to be created in the Active Directory domain. If not specified, defaults to the name of the Active Directory configuration.  # noqa: E501

        :param computer_name: The computer_name of this ActiveDirectory.  # noqa: E501
        :type: str
        """

        self._computer_name = computer_name

    @property
    def directory_servers(self):
        """Gets the directory_servers of this ActiveDirectory.  # noqa: E501

        A list of directory servers that will be used for lookups related to user authorization. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array's configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol.  # noqa: E501

        :return: The directory_servers of this ActiveDirectory.  # noqa: E501
        :rtype: list[str]
        """
        return self._directory_servers

    @directory_servers.setter
    def directory_servers(self, directory_servers):
        """Sets the directory_servers of this ActiveDirectory.

        A list of directory servers that will be used for lookups related to user authorization. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array's configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol.  # noqa: E501

        :param directory_servers: The directory_servers of this ActiveDirectory.  # noqa: E501
        :type: list[str]
        """

        self._directory_servers = directory_servers

    @property
    def domain(self):
        """Gets the domain of this ActiveDirectory.  # noqa: E501

        The Active Directory domain to join.  # noqa: E501

        :return: The domain of this ActiveDirectory.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ActiveDirectory.

        The Active Directory domain to join.  # noqa: E501

        :param domain: The domain of this ActiveDirectory.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def encryption_types(self):
        """Gets the encryption_types of this ActiveDirectory.  # noqa: E501

        The encryption types that are supported for use by clients for Kerberos authentication.  # noqa: E501

        :return: The encryption_types of this ActiveDirectory.  # noqa: E501
        :rtype: list[str]
        """
        return self._encryption_types

    @encryption_types.setter
    def encryption_types(self, encryption_types):
        """Sets the encryption_types of this ActiveDirectory.

        The encryption types that are supported for use by clients for Kerberos authentication.  # noqa: E501

        :param encryption_types: The encryption_types of this ActiveDirectory.  # noqa: E501
        :type: list[str]
        """

        self._encryption_types = encryption_types

    @property
    def join_ou(self):
        """Gets the join_ou of this ActiveDirectory.  # noqa: E501

        The relative distinguished name of the organizational unit in which the computer account was created when joining the domain.  # noqa: E501

        :return: The join_ou of this ActiveDirectory.  # noqa: E501
        :rtype: str
        """
        return self._join_ou

    @join_ou.setter
    def join_ou(self, join_ou):
        """Sets the join_ou of this ActiveDirectory.

        The relative distinguished name of the organizational unit in which the computer account was created when joining the domain.  # noqa: E501

        :param join_ou: The join_ou of this ActiveDirectory.  # noqa: E501
        :type: str
        """

        self._join_ou = join_ou

    @property
    def kerberos_servers(self):
        """Gets the kerberos_servers of this ActiveDirectory.  # noqa: E501

        A list of key distribution servers to use for Kerberos protocol. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array's configured DNS.  # noqa: E501

        :return: The kerberos_servers of this ActiveDirectory.  # noqa: E501
        :rtype: list[str]
        """
        return self._kerberos_servers

    @kerberos_servers.setter
    def kerberos_servers(self, kerberos_servers):
        """Sets the kerberos_servers of this ActiveDirectory.

        A list of key distribution servers to use for Kerberos protocol. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array's configured DNS.  # noqa: E501

        :param kerberos_servers: The kerberos_servers of this ActiveDirectory.  # noqa: E501
        :type: list[str]
        """

        self._kerberos_servers = kerberos_servers

    @property
    def service_principal_names(self):
        """Gets the service_principal_names of this ActiveDirectory.  # noqa: E501

        A list of service principal names registered for the machine account, which can be used for the creation of keys for Kerberos authentication.  # noqa: E501

        :return: The service_principal_names of this ActiveDirectory.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_principal_names

    @service_principal_names.setter
    def service_principal_names(self, service_principal_names):
        """Sets the service_principal_names of this ActiveDirectory.

        A list of service principal names registered for the machine account, which can be used for the creation of keys for Kerberos authentication.  # noqa: E501

        :param service_principal_names: The service_principal_names of this ActiveDirectory.  # noqa: E501
        :type: list[str]
        """

        self._service_principal_names = service_principal_names

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
        if issubclass(ActiveDirectory, dict):
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
        if not isinstance(other, ActiveDirectory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other