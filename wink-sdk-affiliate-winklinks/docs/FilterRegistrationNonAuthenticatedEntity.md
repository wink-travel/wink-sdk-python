# FilterRegistrationNonAuthenticatedEntity


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
from wink_sdk_affiliate_winklinks.models.filter_registration_non_authenticated_entity import FilterRegistrationNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FilterRegistrationNonAuthenticatedEntity from a JSON string
filter_registration_non_authenticated_entity_instance = FilterRegistrationNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(FilterRegistrationNonAuthenticatedEntity.to_json())

# convert the object into a dict
filter_registration_non_authenticated_entity_dict = filter_registration_non_authenticated_entity_instance.to_dict()
# create an instance of FilterRegistrationNonAuthenticatedEntity from a dict
filter_registration_non_authenticated_entity_from_dict = FilterRegistrationNonAuthenticatedEntity.from_dict(filter_registration_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


