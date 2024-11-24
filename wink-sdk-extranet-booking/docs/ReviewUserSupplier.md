# ReviewUserSupplier

User details of creator of booking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email | [optional] 
**telephone** | **str** | Telephone | [optional] 
**full_name** | **str** | Full name | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.review_user_supplier import ReviewUserSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewUserSupplier from a JSON string
review_user_supplier_instance = ReviewUserSupplier.from_json(json)
# print the JSON string representation of the object
print(ReviewUserSupplier.to_json())

# convert the object into a dict
review_user_supplier_dict = review_user_supplier_instance.to_dict()
# create an instance of ReviewUserSupplier from a dict
review_user_supplier_from_dict = ReviewUserSupplier.from_dict(review_user_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


