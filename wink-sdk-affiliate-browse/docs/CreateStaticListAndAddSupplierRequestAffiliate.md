# CreateStaticListAndAddSupplierRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of curated list | 
**supplier_identifier** | **UUID** | Supplier this list should add. | 
**channel_inventory_type** | **str** | Supplier this list should add. | 

## Example

```python
from wink_sdk_affiliate_browse.models.create_static_list_and_add_supplier_request_affiliate import CreateStaticListAndAddSupplierRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStaticListAndAddSupplierRequestAffiliate from a JSON string
create_static_list_and_add_supplier_request_affiliate_instance = CreateStaticListAndAddSupplierRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(CreateStaticListAndAddSupplierRequestAffiliate.to_json())

# convert the object into a dict
create_static_list_and_add_supplier_request_affiliate_dict = create_static_list_and_add_supplier_request_affiliate_instance.to_dict()
# create an instance of CreateStaticListAndAddSupplierRequestAffiliate from a dict
create_static_list_and_add_supplier_request_affiliate_from_dict = CreateStaticListAndAddSupplierRequestAffiliate.from_dict(create_static_list_and_add_supplier_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


