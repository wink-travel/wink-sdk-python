# SubSubCountryBooker

Country sub sub division

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.sub_sub_country_booker import SubSubCountryBooker

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountryBooker from a JSON string
sub_sub_country_booker_instance = SubSubCountryBooker.from_json(json)
# print the JSON string representation of the object
print(SubSubCountryBooker.to_json())

# convert the object into a dict
sub_sub_country_booker_dict = sub_sub_country_booker_instance.to_dict()
# create an instance of SubSubCountryBooker from a dict
sub_sub_country_booker_from_dict = SubSubCountryBooker.from_dict(sub_sub_country_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


