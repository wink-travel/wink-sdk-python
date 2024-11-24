# UpsertPropertyProfileRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stars** | **int** | Hotel star rating. | 
**hotel_chain** | **str** | Hotel chain name if property is part of that chain. | [optional] 
**hotel_brand** | **str** | Hotel brand name if property is part of that brand. | [optional] 
**when_built** | **str** | Year the property was constructed. | [optional] 
**website** | **str** | Property&#39;s brand.com website. | [optional] 
**license_number** | **str** | If the property has a valid license number to run a hotel in their country, add it here. | [optional] 
**number_of_rooms** | **int** | Number of rooms / keys for property | 
**location_category** | **str** | Supported OTA specification &#x60;LOC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**segment_category** | **str** | Supported OTA specification &#x60;SEG&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**hotel_category** | **str** | Supported OTA specification &#x60;PCT&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**architectural_style** | **str** | Supported OTA specification &#x60;ARC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 

## Example

```python
from wink_sdk_extranet_property.models.upsert_property_profile_request_supplier import UpsertPropertyProfileRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertPropertyProfileRequestSupplier from a JSON string
upsert_property_profile_request_supplier_instance = UpsertPropertyProfileRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertPropertyProfileRequestSupplier.to_json())

# convert the object into a dict
upsert_property_profile_request_supplier_dict = upsert_property_profile_request_supplier_instance.to_dict()
# create an instance of UpsertPropertyProfileRequestSupplier from a dict
upsert_property_profile_request_supplier_from_dict = UpsertPropertyProfileRequestSupplier.from_dict(upsert_property_profile_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


