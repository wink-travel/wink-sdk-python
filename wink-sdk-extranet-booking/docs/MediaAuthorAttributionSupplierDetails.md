# MediaAuthorAttributionSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_extranet_booking.models.media_author_attribution_supplier_details import MediaAuthorAttributionSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAuthorAttributionSupplierDetails from a JSON string
media_author_attribution_supplier_details_instance = MediaAuthorAttributionSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(MediaAuthorAttributionSupplierDetails.to_json())

# convert the object into a dict
media_author_attribution_supplier_details_dict = media_author_attribution_supplier_details_instance.to_dict()
# create an instance of MediaAuthorAttributionSupplierDetails from a dict
media_author_attribution_supplier_details_from_dict = MediaAuthorAttributionSupplierDetails.from_dict(media_author_attribution_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


