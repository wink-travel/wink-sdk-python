# FilterRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servlet_name_mappings** | **List[str]** |  | [optional] 
**url_pattern_mappings** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**class_name** | **str** |  | [optional] 
**init_parameters** | **Dict[str, str]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.filter_registration import FilterRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of FilterRegistration from a JSON string
filter_registration_instance = FilterRegistration.from_json(json)
# print the JSON string representation of the object
print(FilterRegistration.to_json())

# convert the object into a dict
filter_registration_dict = filter_registration_instance.to_dict()
# create an instance of FilterRegistration from a dict
filter_registration_from_dict = FilterRegistration.from_dict(filter_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


