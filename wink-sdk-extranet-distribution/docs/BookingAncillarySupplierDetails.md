# BookingAncillarySupplierDetails

Add-on records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Ancillary identifier | 
**hotel_identifier** | **str** | Hotel identifier | 
**type_identifier** | **str** | Travel blocking identifier | 
**transactional_travel_inventory_identifier** | **str** | Travel blocking identifier | 
**name** | **str** | Name of blocking | 
**pricing_type** | **str** | Pricing type | 
**type** | **str** | Inventory type | 
**price** | [**LocalizedPriceSupplierDetails**](LocalizedPriceSupplierDetails.md) |  | 
**start_date** | **datetime** | Date start time when reservation was made for. | 
**end_date** | **datetime** | Date end time when reservation was made for. | 
**attendees** | **int** | Number of guests that are part of this reservation. | [default to 1]
**image_identifier** | **str** | Cloudinary image identifier | 
**image_url** | **str** | Absolute URL to image of blocking | 
**localized_name** | **str** | Name of travel blocking in traveler language (if available). Defaults to English. | 
**localized_description** | **str** | Description of travel blocking in traveler language (if available). Defaults to English. | 
**contact** | [**ContactSupplierDetails**](ContactSupplierDetails.md) |  | 
**address** | [**SimpleAddressSupplierDetails**](SimpleAddressSupplierDetails.md) |  | 
**commissionable** | **bool** |  | 
**mandatory** | **bool** |  | 
**commission** | **float** |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.booking_ancillary_supplier_details import BookingAncillarySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BookingAncillarySupplierDetails from a JSON string
booking_ancillary_supplier_details_instance = BookingAncillarySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BookingAncillarySupplierDetails.to_json())

# convert the object into a dict
booking_ancillary_supplier_details_dict = booking_ancillary_supplier_details_instance.to_dict()
# create an instance of BookingAncillarySupplierDetails from a dict
booking_ancillary_supplier_details_from_dict = BookingAncillarySupplierDetails.from_dict(booking_ancillary_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


