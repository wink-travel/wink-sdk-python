# CancellationPolicyLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique cancellation policy identifier | 
**hotel_identifier** | **UUID** | Property this cancellation is associated with | 
**refundable** | **bool** | Whether this cancellation policy is refundable or not | [default to False]
**advance_cancellation_free_of_charge** | **str** | When the cancellation policy is refundable, this flag can be set and indicates there is more rules involved than just a no-questions-asked refundable. | [optional] 
**refundable_cancellation_charge** | **str** | If advanceCancellationFreeOfCharge rules is not honored, this property explains what the guest will be charged. | [optional] 
**no_show_charge** | **str** | In case the &#39;Refundable cancellation charge&#39; is set, a different no show charge can be applied. | [optional] 
**non_refundable_cancellation_charge** | **str** | When the cancellation policy is non-refundable, this flag can be set and indicates there is more rules involved to calculate what the guest will owe in case of a cancellation. | [optional] 
**non_refundable_deadline** | **str** | The non-refundable charge might can have a deadline. If that deadline passes, the guest might be charged more. | [optional] 
**non_refundable_after_deadline_cancellation_charge** | **str** | If the guest does not honor the non-refundable deadline rule, this charge dictates what she owes after the deadline passes. | [optional] 
**policy_code** | **str** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.cancellation_policy_lightweight_non_authenticated_entity import CancellationPolicyLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyLightweightNonAuthenticatedEntity from a JSON string
cancellation_policy_lightweight_non_authenticated_entity_instance = CancellationPolicyLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
cancellation_policy_lightweight_non_authenticated_entity_dict = cancellation_policy_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of CancellationPolicyLightweightNonAuthenticatedEntity from a dict
cancellation_policy_lightweight_non_authenticated_entity_from_dict = CancellationPolicyLightweightNonAuthenticatedEntity.from_dict(cancellation_policy_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


