# AddOnLocalizedInventorySupplierDetails

Add-ons that are available with this room configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_on** | [**AddOnSupplierDetails**](AddOnSupplierDetails.md) |  | 
**price_list** | [**List[LocalizedTransactionalTravelInventorySupplierDetails]**](LocalizedTransactionalTravelInventorySupplierDetails.md) |  | [optional] 
**channel_inventory_identifier** | **str** | Channel blocking identifier referencing this record. | [optional] 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | [optional] 
**commission** | **float** | The commission percentage. | [optional] 
**direct** | **bool** | Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking. | [default to False]

## Example

```python
from wink_sdk_extranet_distribution.models.add_on_localized_inventory_supplier_details import AddOnLocalizedInventorySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnLocalizedInventorySupplierDetails from a JSON string
add_on_localized_inventory_supplier_details_instance = AddOnLocalizedInventorySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(AddOnLocalizedInventorySupplierDetails.to_json())

# convert the object into a dict
add_on_localized_inventory_supplier_details_dict = add_on_localized_inventory_supplier_details_instance.to_dict()
# create an instance of AddOnLocalizedInventorySupplierDetails from a dict
add_on_localized_inventory_supplier_details_from_dict = AddOnLocalizedInventorySupplierDetails.from_dict(add_on_localized_inventory_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


