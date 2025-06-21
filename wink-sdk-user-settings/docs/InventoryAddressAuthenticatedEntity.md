# InventoryAddressAuthenticatedEntity

Address information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | [optional] 
**county** | **str** | County | [optional] 
**city_geo_name_id** | **str** | Unique city ID | [optional] 
**city_url_name** | **str** | Url name | [optional] 
**city** | **str** | Ascii name of city | [optional] 
**country** | **str** | Country name | [optional] 
**country_code** | **str** | Country code | [optional] 
**country_geo_name_id** | **str** | Country geo name ID | [optional] 
**continent** | **str** | continent | [optional] 

## Example

```python
from wink_sdk_user_settings.models.inventory_address_authenticated_entity import InventoryAddressAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddressAuthenticatedEntity from a JSON string
inventory_address_authenticated_entity_instance = InventoryAddressAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InventoryAddressAuthenticatedEntity.to_json())

# convert the object into a dict
inventory_address_authenticated_entity_dict = inventory_address_authenticated_entity_instance.to_dict()
# create an instance of InventoryAddressAuthenticatedEntity from a dict
inventory_address_authenticated_entity_from_dict = InventoryAddressAuthenticatedEntity.from_dict(inventory_address_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


