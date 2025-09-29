# CreateAffiliate400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.create_affiliate400_response import CreateAffiliate400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAffiliate400Response from a JSON string
create_affiliate400_response_instance = CreateAffiliate400Response.from_json(json)
# print the JSON string representation of the object
print(CreateAffiliate400Response.to_json())

# convert the object into a dict
create_affiliate400_response_dict = create_affiliate400_response_instance.to_dict()
# create an instance of CreateAffiliate400Response from a dict
create_affiliate400_response_from_dict = CreateAffiliate400Response.from_dict(create_affiliate400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


