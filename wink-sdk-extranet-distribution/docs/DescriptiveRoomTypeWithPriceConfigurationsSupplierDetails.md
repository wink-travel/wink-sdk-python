# DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room** | [**GuestRoomSupplierDetails**](GuestRoomSupplierDetails.md) |  | [optional] 
**available** | **bool** |  | [optional] 
**best_price** | [**RoomConfigurationPriceSupplierDetails**](RoomConfigurationPriceSupplierDetails.md) |  | [optional] 
**price_configurations** | [**List[RoomConfigurationPriceSupplierDetails]**](RoomConfigurationPriceSupplierDetails.md) |  | [optional] 
**inaccessible_availability_reason** | [**DescriptiveReasonSupplierDetails**](DescriptiveReasonSupplierDetails.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.descriptive_room_type_with_price_configurations_supplier_details import DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails from a JSON string
descriptive_room_type_with_price_configurations_supplier_details_instance = DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails.to_json())

# convert the object into a dict
descriptive_room_type_with_price_configurations_supplier_details_dict = descriptive_room_type_with_price_configurations_supplier_details_instance.to_dict()
# create an instance of DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails from a dict
descriptive_room_type_with_price_configurations_supplier_details_from_dict = DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails.from_dict(descriptive_room_type_with_price_configurations_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


