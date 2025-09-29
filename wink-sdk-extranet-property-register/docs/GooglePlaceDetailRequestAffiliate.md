# GooglePlaceDetailRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**place_id** | **str** |  | 
**name** | **str** |  | 
**message_from_user** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.google_place_detail_request_affiliate import GooglePlaceDetailRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePlaceDetailRequestAffiliate from a JSON string
google_place_detail_request_affiliate_instance = GooglePlaceDetailRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(GooglePlaceDetailRequestAffiliate.to_json())

# convert the object into a dict
google_place_detail_request_affiliate_dict = google_place_detail_request_affiliate_instance.to_dict()
# create an instance of GooglePlaceDetailRequestAffiliate from a dict
google_place_detail_request_affiliate_from_dict = GooglePlaceDetailRequestAffiliate.from_dict(google_place_detail_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


