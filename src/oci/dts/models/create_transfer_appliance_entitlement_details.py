# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTransferApplianceEntitlementDetails(object):
    """
    CreateTransferApplianceEntitlementDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTransferApplianceEntitlementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTransferApplianceEntitlementDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateTransferApplianceEntitlementDetails.
        :type display_name: str

        :param requestor_name:
            The value to assign to the requestor_name property of this CreateTransferApplianceEntitlementDetails.
        :type requestor_name: str

        :param requestor_email:
            The value to assign to the requestor_email property of this CreateTransferApplianceEntitlementDetails.
        :type requestor_email: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTransferApplianceEntitlementDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTransferApplianceEntitlementDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'requestor_name': 'str',
            'requestor_email': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'requestor_name': 'requestorName',
            'requestor_email': 'requestorEmail',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._requestor_name = None
        self._requestor_email = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateTransferApplianceEntitlementDetails.

        :return: The compartment_id of this CreateTransferApplianceEntitlementDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTransferApplianceEntitlementDetails.

        :param compartment_id: The compartment_id of this CreateTransferApplianceEntitlementDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateTransferApplianceEntitlementDetails.

        :return: The display_name of this CreateTransferApplianceEntitlementDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTransferApplianceEntitlementDetails.

        :param display_name: The display_name of this CreateTransferApplianceEntitlementDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def requestor_name(self):
        """
        Gets the requestor_name of this CreateTransferApplianceEntitlementDetails.

        :return: The requestor_name of this CreateTransferApplianceEntitlementDetails.
        :rtype: str
        """
        return self._requestor_name

    @requestor_name.setter
    def requestor_name(self, requestor_name):
        """
        Sets the requestor_name of this CreateTransferApplianceEntitlementDetails.

        :param requestor_name: The requestor_name of this CreateTransferApplianceEntitlementDetails.
        :type: str
        """
        self._requestor_name = requestor_name

    @property
    def requestor_email(self):
        """
        Gets the requestor_email of this CreateTransferApplianceEntitlementDetails.

        :return: The requestor_email of this CreateTransferApplianceEntitlementDetails.
        :rtype: str
        """
        return self._requestor_email

    @requestor_email.setter
    def requestor_email(self, requestor_email):
        """
        Sets the requestor_email of this CreateTransferApplianceEntitlementDetails.

        :param requestor_email: The requestor_email of this CreateTransferApplianceEntitlementDetails.
        :type: str
        """
        self._requestor_email = requestor_email

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTransferApplianceEntitlementDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateTransferApplianceEntitlementDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTransferApplianceEntitlementDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateTransferApplianceEntitlementDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTransferApplianceEntitlementDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this CreateTransferApplianceEntitlementDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTransferApplianceEntitlementDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :param defined_tags: The defined_tags of this CreateTransferApplianceEntitlementDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other