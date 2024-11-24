# ReviewUserSupplierDetails

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
from wink_sdk_extranet_booking.models.review_user_supplier_details import ReviewUserSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewUserSupplierDetails from a JSON string
review_user_supplier_details_instance = ReviewUserSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ReviewUserSupplierDetails.to_json())

# convert the object into a dict
review_user_supplier_details_dict = review_user_supplier_details_instance.to_dict()
# create an instance of ReviewUserSupplierDetails from a dict
review_user_supplier_details_from_dict = ReviewUserSupplierDetails.from_dict(review_user_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


