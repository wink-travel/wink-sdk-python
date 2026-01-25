# PeriodForPropertyRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | The property to query for. | 
**start_date** | **date** | Start of period. | 
**period_in_days** | **int** | The period to query within. | [optional] [default to 5]
**adults** | **int** | The period to query within. | [optional] [default to 2]
**language** | **str** | The language to display room type name. | [default to 'en']
**currency** | **str** | The currency to display prices in. | [optional] [default to 'USD']
**rate_plan_name_matches_reg_ex** | **str** | A regular expression to apply to the rate plan name | [optional] 

## Example

```python
from wink_sdk_inventory.models.period_for_property_request_non_authenticated_entity import PeriodForPropertyRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodForPropertyRequestNonAuthenticatedEntity from a JSON string
period_for_property_request_non_authenticated_entity_instance = PeriodForPropertyRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PeriodForPropertyRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
period_for_property_request_non_authenticated_entity_dict = period_for_property_request_non_authenticated_entity_instance.to_dict()
# create an instance of PeriodForPropertyRequestNonAuthenticatedEntity from a dict
period_for_property_request_non_authenticated_entity_from_dict = PeriodForPropertyRequestNonAuthenticatedEntity.from_dict(period_for_property_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


