# RatePlanViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**rate_plan** | [**RatePlanSupplier**](RatePlanSupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_monetize.models.rate_plan_view_supplier import RatePlanViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanViewSupplier from a JSON string
rate_plan_view_supplier_instance = RatePlanViewSupplier.from_json(json)
# print the JSON string representation of the object
print(RatePlanViewSupplier.to_json())

# convert the object into a dict
rate_plan_view_supplier_dict = rate_plan_view_supplier_instance.to_dict()
# create an instance of RatePlanViewSupplier from a dict
rate_plan_view_supplier_from_dict = RatePlanViewSupplier.from_dict(rate_plan_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


