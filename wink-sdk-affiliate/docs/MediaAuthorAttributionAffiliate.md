# MediaAuthorAttributionAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_affiliate.models.media_author_attribution_affiliate import MediaAuthorAttributionAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAuthorAttributionAffiliate from a JSON string
media_author_attribution_affiliate_instance = MediaAuthorAttributionAffiliate.from_json(json)
# print the JSON string representation of the object
print(MediaAuthorAttributionAffiliate.to_json())

# convert the object into a dict
media_author_attribution_affiliate_dict = media_author_attribution_affiliate_instance.to_dict()
# create an instance of MediaAuthorAttributionAffiliate from a dict
media_author_attribution_affiliate_from_dict = MediaAuthorAttributionAffiliate.from_dict(media_author_attribution_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


