# CheckoutResponseAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[PayableContractResponseAuthenticatedEntity]**](PayableContractResponseAuthenticatedEntity.md) | TripPay&#39;s ID to be used in conjunction with TripPay&#39;s reactive widget | 

## Example

```python
from wink_sdk_booking.models.checkout_response_authenticated_entity import CheckoutResponseAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutResponseAuthenticatedEntity from a JSON string
checkout_response_authenticated_entity_instance = CheckoutResponseAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CheckoutResponseAuthenticatedEntity.to_json())

# convert the object into a dict
checkout_response_authenticated_entity_dict = checkout_response_authenticated_entity_instance.to_dict()
# create an instance of CheckoutResponseAuthenticatedEntity from a dict
checkout_response_authenticated_entity_from_dict = CheckoutResponseAuthenticatedEntity.from_dict(checkout_response_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


