# CancellationPolicyException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **str** | Cancellation policy | 
**cancellation_policy** | [**CancellationPolicy**](CancellationPolicy.md) |  | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_extranet_monetize.models.cancellation_policy_exception import CancellationPolicyException

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyException from a JSON string
cancellation_policy_exception_instance = CancellationPolicyException.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyException.to_json())

# convert the object into a dict
cancellation_policy_exception_dict = cancellation_policy_exception_instance.to_dict()
# create an instance of CancellationPolicyException from a dict
cancellation_policy_exception_from_dict = CancellationPolicyException.from_dict(cancellation_policy_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


