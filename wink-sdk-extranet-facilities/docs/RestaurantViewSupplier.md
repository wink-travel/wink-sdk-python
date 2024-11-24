# RestaurantViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**restaurant** | [**RestaurantSupplier**](RestaurantSupplier.md) |  | [optional] 
**featured_image_identifier** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_facilities.models.restaurant_view_supplier import RestaurantViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantViewSupplier from a JSON string
restaurant_view_supplier_instance = RestaurantViewSupplier.from_json(json)
# print the JSON string representation of the object
print(RestaurantViewSupplier.to_json())

# convert the object into a dict
restaurant_view_supplier_dict = restaurant_view_supplier_instance.to_dict()
# create an instance of RestaurantViewSupplier from a dict
restaurant_view_supplier_from_dict = RestaurantViewSupplier.from_dict(restaurant_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


