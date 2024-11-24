# ReviewResponseSupplier

Property response to review.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_from_hotel** | **str** | Texual response from hotel to user&#39;s review. | 
**approved_text** | **bool** | Property approves the use of guest review text with property profile. | 
**approved_image** | **bool** | Property approves the use of guest generated image with property profile. | 

## Example

```python
from wink_sdk_extranet_booking.models.review_response_supplier import ReviewResponseSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewResponseSupplier from a JSON string
review_response_supplier_instance = ReviewResponseSupplier.from_json(json)
# print the JSON string representation of the object
print(ReviewResponseSupplier.to_json())

# convert the object into a dict
review_response_supplier_dict = review_response_supplier_instance.to_dict()
# create an instance of ReviewResponseSupplier from a dict
review_response_supplier_from_dict = ReviewResponseSupplier.from_dict(review_response_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


