# TransactionalTravelInventorySupplier

This is one bookable item that can stand alongside a restaurant / meeting room etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique transactional identifier | 
**name** | **str** | Internal name of transactional blocking. | 
**descriptions** | [**List[SimpleDescriptionSupplier]**](SimpleDescriptionSupplier.md) | Localized descriptions describing inventory. | 
**pricing_type** | **str** | How this blocking item should be priced. | 
**base_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Base price of booking this blocking. | 
**discounted_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | If you are selling this blocking at a discount, indicate the discounted selling price. Leave empty if there is no discount. | 
**multimedias** | [**List[SimpleMultimediaSupplier]**](SimpleMultimediaSupplier.md) | List of images / videos of item. | [optional] 
**min_pax** | **int** | Whether there is a limit to minimum group size. | [optional] 
**max_pax** | **int** | Whether there is a limit to maximum group size. | [optional] 
**percent_premium** | **float** | Calculates the percent difference between basePrice and discountedPrice. | [optional] 
**percent_discount** | **float** | Calculates the percent difference between basePrice and discountedPrice. | [optional] 

## Example

```python
from wink_sdk_extranet_experiences.models.transactional_travel_inventory_supplier import TransactionalTravelInventorySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionalTravelInventorySupplier from a JSON string
transactional_travel_inventory_supplier_instance = TransactionalTravelInventorySupplier.from_json(json)
# print the JSON string representation of the object
print(TransactionalTravelInventorySupplier.to_json())

# convert the object into a dict
transactional_travel_inventory_supplier_dict = transactional_travel_inventory_supplier_instance.to_dict()
# create an instance of TransactionalTravelInventorySupplier from a dict
transactional_travel_inventory_supplier_from_dict = TransactionalTravelInventorySupplier.from_dict(transactional_travel_inventory_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


