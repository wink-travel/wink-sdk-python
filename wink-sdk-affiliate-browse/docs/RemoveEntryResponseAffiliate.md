# RemoveEntryResponseAffiliate

Response object for when a system document is removed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of removed document | [optional] 
**success** | **bool** | Whether the removal was successful or not. | [optional] 
**message** | **str** | Message with additional information; mostly if the removal request was a failure. | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.remove_entry_response_affiliate import RemoveEntryResponseAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveEntryResponseAffiliate from a JSON string
remove_entry_response_affiliate_instance = RemoveEntryResponseAffiliate.from_json(json)
# print the JSON string representation of the object
print(RemoveEntryResponseAffiliate.to_json())

# convert the object into a dict
remove_entry_response_affiliate_dict = remove_entry_response_affiliate_instance.to_dict()
# create an instance of RemoveEntryResponseAffiliate from a dict
remove_entry_response_affiliate_from_dict = RemoveEntryResponseAffiliate.from_dict(remove_entry_response_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


