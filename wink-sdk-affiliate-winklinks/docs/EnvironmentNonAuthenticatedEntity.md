# EnvironmentNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_profiles** | **List[str]** |  | [optional] 
**default_profiles** | **List[str]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.environment_non_authenticated_entity import EnvironmentNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentNonAuthenticatedEntity from a JSON string
environment_non_authenticated_entity_instance = EnvironmentNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(EnvironmentNonAuthenticatedEntity.to_json())

# convert the object into a dict
environment_non_authenticated_entity_dict = environment_non_authenticated_entity_instance.to_dict()
# create an instance of EnvironmentNonAuthenticatedEntity from a dict
environment_non_authenticated_entity_from_dict = EnvironmentNonAuthenticatedEntity.from_dict(environment_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


