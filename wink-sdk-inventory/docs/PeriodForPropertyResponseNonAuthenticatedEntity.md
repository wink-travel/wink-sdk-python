# PeriodForPropertyResponseNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | The property to query for. | 
**name** | **str** | The property name. | 
**adults** | **int** | The actual amount of adults as determined by the hotel&#39;s policy | 
**list** | [**List[RoomTypeBestPriceForDateRangeNonAuthenticatedEntity]**](RoomTypeBestPriceForDateRangeNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_inventory.models.period_for_property_response_non_authenticated_entity import PeriodForPropertyResponseNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodForPropertyResponseNonAuthenticatedEntity from a JSON string
period_for_property_response_non_authenticated_entity_instance = PeriodForPropertyResponseNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PeriodForPropertyResponseNonAuthenticatedEntity.to_json())

# convert the object into a dict
period_for_property_response_non_authenticated_entity_dict = period_for_property_response_non_authenticated_entity_instance.to_dict()
# create an instance of PeriodForPropertyResponseNonAuthenticatedEntity from a dict
period_for_property_response_non_authenticated_entity_from_dict = PeriodForPropertyResponseNonAuthenticatedEntity.from_dict(period_for_property_response_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


