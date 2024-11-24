# GooglePlaceDetailRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**place_id** | **str** | Unique ID | 
**name** | **str** | Name of lead | 
**message_from_user** | **str** | A personalized message from the inviter | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.google_place_detail_request_supplier import GooglePlaceDetailRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePlaceDetailRequestSupplier from a JSON string
google_place_detail_request_supplier_instance = GooglePlaceDetailRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(GooglePlaceDetailRequestSupplier.to_json())

# convert the object into a dict
google_place_detail_request_supplier_dict = google_place_detail_request_supplier_instance.to_dict()
# create an instance of GooglePlaceDetailRequestSupplier from a dict
google_place_detail_request_supplier_from_dict = GooglePlaceDetailRequestSupplier.from_dict(google_place_detail_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


