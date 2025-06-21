# ImageAttributionAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_affiliate.models.image_attribution_affiliate import ImageAttributionAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributionAffiliate from a JSON string
image_attribution_affiliate_instance = ImageAttributionAffiliate.from_json(json)
# print the JSON string representation of the object
print(ImageAttributionAffiliate.to_json())

# convert the object into a dict
image_attribution_affiliate_dict = image_attribution_affiliate_instance.to_dict()
# create an instance of ImageAttributionAffiliate from a dict
image_attribution_affiliate_from_dict = ImageAttributionAffiliate.from_dict(image_attribution_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


