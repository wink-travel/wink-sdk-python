# BedroomConfigurationAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique identifier | 
**name** | **str** | Name of layout | 
**bedroom_list** | [**List[BedroomAuthenticatedEntity]**](BedroomAuthenticatedEntity.md) | A room type can have more than one bedroom configuration. | 

## Example

```python
from wink_sdk_booking.models.bedroom_configuration_authenticated_entity import BedroomConfigurationAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomConfigurationAuthenticatedEntity from a JSON string
bedroom_configuration_authenticated_entity_instance = BedroomConfigurationAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(BedroomConfigurationAuthenticatedEntity.to_json())

# convert the object into a dict
bedroom_configuration_authenticated_entity_dict = bedroom_configuration_authenticated_entity_instance.to_dict()
# create an instance of BedroomConfigurationAuthenticatedEntity from a dict
bedroom_configuration_authenticated_entity_from_dict = BedroomConfigurationAuthenticatedEntity.from_dict(bedroom_configuration_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


