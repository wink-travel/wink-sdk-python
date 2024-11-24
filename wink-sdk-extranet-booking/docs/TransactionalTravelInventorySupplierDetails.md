# TransactionalTravelInventorySupplierDetails

This is one bookable item that can stand alongside a restaurant / meeting room etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique transactional identifier | 
**name** | **str** | Internal name of transactional blocking. | 
**descriptions** | [**List[SimpleDescriptionSupplierDetails]**](SimpleDescriptionSupplierDetails.md) | Localized descriptions describing blocking. | 
**pricing_type** | **str** | How this blocking item should be priced. | 
**base_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**discounted_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**multimedias** | [**List[SimpleMultimediaSupplierDetails]**](SimpleMultimediaSupplierDetails.md) | List of images / videos of item. | [optional] 
**min_pax** | **int** | Whether there is a limit to minimum group size. | [optional] 
**max_pax** | **int** | Whether there is a limit to maximum group size. | [optional] 
**percent_premium** | **float** | Calculates the percent difference between basePrice and discountedPrice. | [optional] 
**percent_discount** | **float** | Calculates the percent difference between basePrice and discountedPrice. | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.transactional_travel_inventory_supplier_details import TransactionalTravelInventorySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionalTravelInventorySupplierDetails from a JSON string
transactional_travel_inventory_supplier_details_instance = TransactionalTravelInventorySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(TransactionalTravelInventorySupplierDetails.to_json())

# convert the object into a dict
transactional_travel_inventory_supplier_details_dict = transactional_travel_inventory_supplier_details_instance.to_dict()
# create an instance of TransactionalTravelInventorySupplierDetails from a dict
transactional_travel_inventory_supplier_details_from_dict = TransactionalTravelInventorySupplierDetails.from_dict(transactional_travel_inventory_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


