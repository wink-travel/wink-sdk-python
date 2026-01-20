# UpdatePropertyAmenitiesAndServicesRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_amenity_codes** | **List[str]** | Supported OTA specification &#x60;HAC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**property_accessibility_codes** | **List[str]** | Supported OTA specification &#x60;PHY&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**property_security_codes** | **List[str]** | Supported OTA specification &#x60;SEC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.update_property_amenities_and_services_request_supplier import UpdatePropertyAmenitiesAndServicesRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePropertyAmenitiesAndServicesRequestSupplier from a JSON string
update_property_amenities_and_services_request_supplier_instance = UpdatePropertyAmenitiesAndServicesRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpdatePropertyAmenitiesAndServicesRequestSupplier.to_json())

# convert the object into a dict
update_property_amenities_and_services_request_supplier_dict = update_property_amenities_and_services_request_supplier_instance.to_dict()
# create an instance of UpdatePropertyAmenitiesAndServicesRequestSupplier from a dict
update_property_amenities_and_services_request_supplier_from_dict = UpdatePropertyAmenitiesAndServicesRequestSupplier.from_dict(update_property_amenities_and_services_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


