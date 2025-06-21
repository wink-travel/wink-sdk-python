# UserSessionNonAuthenticatedEntity

User session information containing itinerary and other user related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itinerary** | [**ItineraryNonAuthenticatedEntity**](ItineraryNonAuthenticatedEntity.md) | Dates and travel info. | 
**language** | **str** | User&#39;s language preference | [optional] 
**currency** | **str** | User&#39;s currency preference | [optional] 
**promotional_codes** | **List[object]** |  | [optional] 
**selected_room_configuration_index** | **int** | User can pass the current room configuration index to retrieve rates specifically for that room configuration. | [optional] 
**lifestyle** | **str** | The preferred user lifestyle. | [optional] 

## Example

```python
from wink_sdk_inventory.models.user_session_non_authenticated_entity import UserSessionNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UserSessionNonAuthenticatedEntity from a JSON string
user_session_non_authenticated_entity_instance = UserSessionNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UserSessionNonAuthenticatedEntity.to_json())

# convert the object into a dict
user_session_non_authenticated_entity_dict = user_session_non_authenticated_entity_instance.to_dict()
# create an instance of UserSessionNonAuthenticatedEntity from a dict
user_session_non_authenticated_entity_from_dict = UserSessionNonAuthenticatedEntity.from_dict(user_session_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


