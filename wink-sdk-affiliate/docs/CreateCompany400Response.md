# CreateCompany400Response


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
from wink_sdk_affiliate.models.create_company400_response import CreateCompany400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompany400Response from a JSON string
create_company400_response_instance = CreateCompany400Response.from_json(json)
# print the JSON string representation of the object
print(CreateCompany400Response.to_json())

# convert the object into a dict
create_company400_response_dict = create_company400_response_instance.to_dict()
# create an instance of CreateCompany400Response from a dict
create_company400_response_from_dict = CreateCompany400Response.from_dict(create_company400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


