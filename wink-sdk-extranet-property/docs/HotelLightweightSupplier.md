# HotelLightweightSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Unique hotel identifier | 
**name** | **str** | Unique hotel trade name. The hotel name must be unique. If there are multiple hotels with the same name, we recommend appending destination to the name. [Verify uniqueness here](#operation/isHotelNameUnique). | 
**url_name** | **str** | Unique url-friendly slug to identify property | 
**currency_code** | **str** | Currency code | 
**status** | **str** | wink.travel sets this status as the hotel moves through the payment workflow and manually for approval. | [default to 'WAITING_ON_CONTRACT']
**external_status** | **str** | Property goes active by changing externalStatus from 6 (Inactive) to 1 (Active) according to OTA property status. | [default to '6']
**stars** | **int** | Hotel star rating. | [optional] 
**number_of_rooms** | **int** | Number of rooms / keys for property | 
**active** | **bool** | Property is both approved and activated. | [optional] 
**property_active** | **bool** | Property activated itself and went live. | [optional] 
**platform_active** | **bool** | Platform approved property. | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.hotel_lightweight_supplier import HotelLightweightSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of HotelLightweightSupplier from a JSON string
hotel_lightweight_supplier_instance = HotelLightweightSupplier.from_json(json)
# print the JSON string representation of the object
print(HotelLightweightSupplier.to_json())

# convert the object into a dict
hotel_lightweight_supplier_dict = hotel_lightweight_supplier_instance.to_dict()
# create an instance of HotelLightweightSupplier from a dict
hotel_lightweight_supplier_from_dict = HotelLightweightSupplier.from_dict(hotel_lightweight_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


