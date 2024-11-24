# VerifyRatesRequestSupplierDetails

Rate request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**ChannelNameSupplierDetails**](ChannelNameSupplierDetails.md) |  | 
**stay_start_date** | **date** | Arrival date | 
**stay_end_date** | **date** | Departure date | 
**room_configurations** | [**List[RoomConfigurationSupplierDetails]**](RoomConfigurationSupplierDetails.md) |  | 
**currency** | **str** | Display currency | 
**booking_date** | **date** | The booking start date | [optional] 
**sell_start_date** | **date** | The sell start date | [optional] 
**sell_end_date** | **date** | The sell end date | [optional] 
**promotion** | **str** | A promo code | [optional] 
**city** | [**GeoIPSupplierDetails**](GeoIPSupplierDetails.md) |  | [optional] 
**country** | [**GeoNameCountrySupplierDetails**](GeoNameCountrySupplierDetails.md) |  | [optional] 
**continent** | **str** | A booker coming from a specific continent | [optional] 
**ip_number** | **str** | A booker coming from a specific IP number | [optional] 
**timezone** | **str** | A booker coming from a specific timezone | [optional] 
**latitude** | **float** | A booker coming from a specific latitude | [optional] 
**longitude** | **float** | A booker coming from a specific longitude | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.verify_rates_request_supplier_details import VerifyRatesRequestSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyRatesRequestSupplierDetails from a JSON string
verify_rates_request_supplier_details_instance = VerifyRatesRequestSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(VerifyRatesRequestSupplierDetails.to_json())

# convert the object into a dict
verify_rates_request_supplier_details_dict = verify_rates_request_supplier_details_instance.to_dict()
# create an instance of VerifyRatesRequestSupplierDetails from a dict
verify_rates_request_supplier_details_from_dict = VerifyRatesRequestSupplierDetails.from_dict(verify_rates_request_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


