# KeyValuePairAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value that should be persisted. | 
**label** | **str** | English readable text of the value. | 

## Example

```python
from wink_sdk_affiliate.models.key_value_pair_affiliate import KeyValuePairAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairAffiliate from a JSON string
key_value_pair_affiliate_instance = KeyValuePairAffiliate.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairAffiliate.to_json())

# convert the object into a dict
key_value_pair_affiliate_dict = key_value_pair_affiliate_instance.to_dict()
# create an instance of KeyValuePairAffiliate from a dict
key_value_pair_affiliate_from_dict = KeyValuePairAffiliate.from_dict(key_value_pair_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


