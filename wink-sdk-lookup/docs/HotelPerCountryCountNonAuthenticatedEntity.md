# HotelPerCountryCountNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.hotel_per_country_count_non_authenticated_entity import HotelPerCountryCountNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HotelPerCountryCountNonAuthenticatedEntity from a JSON string
hotel_per_country_count_non_authenticated_entity_instance = HotelPerCountryCountNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(HotelPerCountryCountNonAuthenticatedEntity.to_json())

# convert the object into a dict
hotel_per_country_count_non_authenticated_entity_dict = hotel_per_country_count_non_authenticated_entity_instance.to_dict()
# create an instance of HotelPerCountryCountNonAuthenticatedEntity from a dict
hotel_per_country_count_non_authenticated_entity_from_dict = HotelPerCountryCountNonAuthenticatedEntity.from_dict(hotel_per_country_count_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


