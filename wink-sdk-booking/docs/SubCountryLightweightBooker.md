# SubCountryLightweightBooker

Country subdivision such as a state or province

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sub-country name | [optional] 
**ascii_name** | **str** | Sub-country ascii name | [optional] 
**geo_name_id** | **str** | Sub-country GeoNames identifier | [optional] 

## Example

```python
from wink_sdk_booking.models.sub_country_lightweight_booker import SubCountryLightweightBooker

# TODO update the JSON string below
json = "{}"
# create an instance of SubCountryLightweightBooker from a JSON string
sub_country_lightweight_booker_instance = SubCountryLightweightBooker.from_json(json)
# print the JSON string representation of the object
print(SubCountryLightweightBooker.to_json())

# convert the object into a dict
sub_country_lightweight_booker_dict = sub_country_lightweight_booker_instance.to_dict()
# create an instance of SubCountryLightweightBooker from a dict
sub_country_lightweight_booker_from_dict = SubCountryLightweightBooker.from_dict(sub_country_lightweight_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


