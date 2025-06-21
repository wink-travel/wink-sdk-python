# LocalizedTransactionalTravelInventoryNonAuthenticatedEntity

This is one localized bookable item that can stand alongside a restaurant / meeting room etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique transactional identifier | 
**name** | **str** | Internal name of transactional blocking. | 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) |  | 
**pricing_type** | **str** | How this blocking item should be priced. | 
**price** | [**LocalizedPriceNonAuthenticatedEntity**](LocalizedPriceNonAuthenticatedEntity.md) | Localized price | 
**multimedias** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) |  | [optional] 
**min_pax** | **int** | Whether there is a limit to minimum group size. | [optional] 
**max_pax** | **int** | Whether there is a limit to maximum group size. | [optional] 
**offer_details** | [**List[LocalizedDescriptionNonAuthenticatedEntity]**](LocalizedDescriptionNonAuthenticatedEntity.md) | Localized offer details if rate plan discount applies. | [optional] 
**promotion** | **str** | If a package is linked to a rate plan the user could be entitled to a promotional discount if she enters a code. When this field is populated, it means the discount was applied to the package. | [optional] 

## Example

```python
from wink_sdk_lookup.models.localized_transactional_travel_inventory_non_authenticated_entity import LocalizedTransactionalTravelInventoryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedTransactionalTravelInventoryNonAuthenticatedEntity from a JSON string
localized_transactional_travel_inventory_non_authenticated_entity_instance = LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.to_json())

# convert the object into a dict
localized_transactional_travel_inventory_non_authenticated_entity_dict = localized_transactional_travel_inventory_non_authenticated_entity_instance.to_dict()
# create an instance of LocalizedTransactionalTravelInventoryNonAuthenticatedEntity from a dict
localized_transactional_travel_inventory_non_authenticated_entity_from_dict = LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.from_dict(localized_transactional_travel_inventory_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


