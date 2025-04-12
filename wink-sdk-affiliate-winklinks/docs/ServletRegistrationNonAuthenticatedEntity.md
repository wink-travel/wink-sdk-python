# ServletRegistrationNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | **List[str]** |  | [optional] 
**run_as_role** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**class_name** | **str** |  | [optional] 
**init_parameters** | **Dict[str, str]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.servlet_registration_non_authenticated_entity import ServletRegistrationNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ServletRegistrationNonAuthenticatedEntity from a JSON string
servlet_registration_non_authenticated_entity_instance = ServletRegistrationNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ServletRegistrationNonAuthenticatedEntity.to_json())

# convert the object into a dict
servlet_registration_non_authenticated_entity_dict = servlet_registration_non_authenticated_entity_instance.to_dict()
# create an instance of ServletRegistrationNonAuthenticatedEntity from a dict
servlet_registration_non_authenticated_entity_from_dict = ServletRegistrationNonAuthenticatedEntity.from_dict(servlet_registration_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


