# CreateStaticSellerListAndAddSupplierRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of curated list | 
**supplier_identifier** | **str** | Supplier this list should add. | 
**channel_inventory_type** | **str** | Supplier this list should add. | 

## Example

```python
from wink_sdk_affiliate_browse.models.create_static_seller_list_and_add_supplier_request_affiliate import CreateStaticSellerListAndAddSupplierRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStaticSellerListAndAddSupplierRequestAffiliate from a JSON string
create_static_seller_list_and_add_supplier_request_affiliate_instance = CreateStaticSellerListAndAddSupplierRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(CreateStaticSellerListAndAddSupplierRequestAffiliate.to_json())

# convert the object into a dict
create_static_seller_list_and_add_supplier_request_affiliate_dict = create_static_seller_list_and_add_supplier_request_affiliate_instance.to_dict()
# create an instance of CreateStaticSellerListAndAddSupplierRequestAffiliate from a dict
create_static_seller_list_and_add_supplier_request_affiliate_from_dict = CreateStaticSellerListAndAddSupplierRequestAffiliate.from_dict(create_static_seller_list_and_add_supplier_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


