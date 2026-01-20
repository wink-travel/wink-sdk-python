# CheckoutRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shopping_cart_identifier** | **str** | Shopping cart to send to TripPay | 
**customization_identifier** | **str** | Wink affiliate customization | [optional] 
**redirect_url** | **str** | Wink affiliate customization | [default to 'https://ota.wink.travel/thank-you']

## Example

```python
from wink_sdk_booking.models.checkout_request_authenticated_entity import CheckoutRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutRequestAuthenticatedEntity from a JSON string
checkout_request_authenticated_entity_instance = CheckoutRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CheckoutRequestAuthenticatedEntity.to_json())

# convert the object into a dict
checkout_request_authenticated_entity_dict = checkout_request_authenticated_entity_instance.to_dict()
# create an instance of CheckoutRequestAuthenticatedEntity from a dict
checkout_request_authenticated_entity_from_dict = CheckoutRequestAuthenticatedEntity.from_dict(checkout_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


