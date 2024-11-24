# UniqueRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name we want to check uniqueness for | 
**identifier** | **str** | An optional accompanying identifier so it doesn&#39;t check itself on an update | [optional] 

## Example

```python
from wink_sdk_affiliate.models.unique_request_affiliate import UniqueRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueRequestAffiliate from a JSON string
unique_request_affiliate_instance = UniqueRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UniqueRequestAffiliate.to_json())

# convert the object into a dict
unique_request_affiliate_dict = unique_request_affiliate_instance.to_dict()
# create an instance of UniqueRequestAffiliate from a dict
unique_request_affiliate_from_dict = UniqueRequestAffiliate.from_dict(unique_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


