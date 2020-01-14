# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MoveCompartmentDetails(object):
    """
    MoveCompartmentDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MoveCompartmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_compartment_id:
            The value to assign to the target_compartment_id property of this MoveCompartmentDetails.
        :type target_compartment_id: str

        """
        self.swagger_types = {
            'target_compartment_id': 'str'
        }

        self.attribute_map = {
            'target_compartment_id': 'targetCompartmentId'
        }

        self._target_compartment_id = None

    @property
    def target_compartment_id(self):
        """
        **[Required]** Gets the target_compartment_id of this MoveCompartmentDetails.
        The `OCID`__ of the destination compartment
        into which to move the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The target_compartment_id of this MoveCompartmentDetails.
        :rtype: str
        """
        return self._target_compartment_id

    @target_compartment_id.setter
    def target_compartment_id(self, target_compartment_id):
        """
        Sets the target_compartment_id of this MoveCompartmentDetails.
        The `OCID`__ of the destination compartment
        into which to move the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param target_compartment_id: The target_compartment_id of this MoveCompartmentDetails.
        :type: str
        """
        self._target_compartment_id = target_compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other