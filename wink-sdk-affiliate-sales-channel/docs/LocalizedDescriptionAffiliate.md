# LocalizedDescriptionAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_affiliate_sales_channel.models.localized_description_affiliate import LocalizedDescriptionAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedDescriptionAffiliate from a JSON string
localized_description_affiliate_instance = LocalizedDescriptionAffiliate.from_json(json)
# print the JSON string representation of the object
print(LocalizedDescriptionAffiliate.to_json())

# convert the object into a dict
localized_description_affiliate_dict = localized_description_affiliate_instance.to_dict()
# create an instance of LocalizedDescriptionAffiliate from a dict
localized_description_affiliate_from_dict = LocalizedDescriptionAffiliate.from_dict(localized_description_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


