# UpdateCuratedList400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.update_curated_list400_response import UpdateCuratedList400Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCuratedList400Response from a JSON string
update_curated_list400_response_instance = UpdateCuratedList400Response.from_json(json)
# print the JSON string representation of the object
print(UpdateCuratedList400Response.to_json())

# convert the object into a dict
update_curated_list400_response_dict = update_curated_list400_response_instance.to_dict()
# create an instance of UpdateCuratedList400Response from a dict
update_curated_list400_response_from_dict = UpdateCuratedList400Response.from_dict(update_curated_list400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


