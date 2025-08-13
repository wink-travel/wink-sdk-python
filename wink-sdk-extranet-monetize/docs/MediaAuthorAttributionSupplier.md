# MediaAuthorAttributionSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_extranet_monetize.models.media_author_attribution_supplier import MediaAuthorAttributionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAuthorAttributionSupplier from a JSON string
media_author_attribution_supplier_instance = MediaAuthorAttributionSupplier.from_json(json)
# print the JSON string representation of the object
print(MediaAuthorAttributionSupplier.to_json())

# convert the object into a dict
media_author_attribution_supplier_dict = media_author_attribution_supplier_instance.to_dict()
# create an instance of MediaAuthorAttributionSupplier from a dict
media_author_attribution_supplier_from_dict = MediaAuthorAttributionSupplier.from_dict(media_author_attribution_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


