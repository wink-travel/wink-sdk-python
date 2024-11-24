# SimpleDescriptionAffiliate

Localized media captions to give user some context about where this media was taken.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | [optional] 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_affiliate_sales_channel.models.simple_description_affiliate import SimpleDescriptionAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDescriptionAffiliate from a JSON string
simple_description_affiliate_instance = SimpleDescriptionAffiliate.from_json(json)
# print the JSON string representation of the object
print(SimpleDescriptionAffiliate.to_json())

# convert the object into a dict
simple_description_affiliate_dict = simple_description_affiliate_instance.to_dict()
# create an instance of SimpleDescriptionAffiliate from a dict
simple_description_affiliate_from_dict = SimpleDescriptionAffiliate.from_dict(simple_description_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


