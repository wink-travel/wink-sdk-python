# DescriptiveRoomSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**room_name** | **str** |  | [optional] 
**accessible_master_rates** | [**List[MasterRateSupplierDetails]**](MasterRateSupplierDetails.md) |  | [optional] 
**inaccessible_master_rates** | [**List[DescriptiveReasonSupplierDetails]**](DescriptiveReasonSupplierDetails.md) |  | [optional] 
**accessible_inventory** | [**List[InventorySupplierDetails]**](InventorySupplierDetails.md) |  | [optional] 
**accessible_rate_plans** | [**List[DescriptiveReasonSupplierDetails]**](DescriptiveReasonSupplierDetails.md) |  | [optional] 
**inaccessible_rate_plans** | [**List[DescriptiveReasonSupplierDetails]**](DescriptiveReasonSupplierDetails.md) |  | [optional] 
**accessible_availability** | [**List[DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails]**](DescriptiveRoomTypeWithPriceConfigurationsSupplierDetails.md) |  | [optional] 
**inaccessible_availability** | [**List[DescriptiveReasonSupplierDetails]**](DescriptiveReasonSupplierDetails.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.descriptive_room_supplier_details import DescriptiveRoomSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptiveRoomSupplierDetails from a JSON string
descriptive_room_supplier_details_instance = DescriptiveRoomSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(DescriptiveRoomSupplierDetails.to_json())

# convert the object into a dict
descriptive_room_supplier_details_dict = descriptive_room_supplier_details_instance.to_dict()
# create an instance of DescriptiveRoomSupplierDetails from a dict
descriptive_room_supplier_details_from_dict = DescriptiveRoomSupplierDetails.from_dict(descriptive_room_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


