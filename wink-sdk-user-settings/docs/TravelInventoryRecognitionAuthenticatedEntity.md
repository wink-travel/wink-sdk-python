# TravelInventoryRecognitionAuthenticatedEntity

Recognition for the ancillary blocking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Recognition identifier. | 
**category** | **str** | Recognition category. | 
**type** | **str** | Type of rating system the recognition operated on. This allows us to display the score properly. | 
**provider** | **str** | The name of the entity that administers this recognition. | 
**rating** | **float** | The actual award or rating received by the hotel facility. | 
**max_rating** | **float** | Use this to let hotels indicate what the total score for this award is. | 
**var_date** | **date** | The date the award was received | [optional] 
**official_appointment_ind** | **bool** | When true, this indicates the property has received official permission from the award provider to use the rating in publications and marketing materials; when false this permission has not been granted. | [optional] 
**rating_symbol** | **str** | Provides the symbol used in the rating. Used in conjunction with the Rating. | [optional] 

## Example

```python
from wink_sdk_user_settings.models.travel_inventory_recognition_authenticated_entity import TravelInventoryRecognitionAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TravelInventoryRecognitionAuthenticatedEntity from a JSON string
travel_inventory_recognition_authenticated_entity_instance = TravelInventoryRecognitionAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(TravelInventoryRecognitionAuthenticatedEntity.to_json())

# convert the object into a dict
travel_inventory_recognition_authenticated_entity_dict = travel_inventory_recognition_authenticated_entity_instance.to_dict()
# create an instance of TravelInventoryRecognitionAuthenticatedEntity from a dict
travel_inventory_recognition_authenticated_entity_from_dict = TravelInventoryRecognitionAuthenticatedEntity.from_dict(travel_inventory_recognition_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


