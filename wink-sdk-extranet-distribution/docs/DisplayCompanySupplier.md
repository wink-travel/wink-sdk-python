# DisplayCompanySupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**owner** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) |  | 
**city** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) |  | 
**country** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) |  | 
**continent** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) |  | 
**name** | **str** |  | 
**owner_name** | **str** |  | 
**url_name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 
**enabled** | **bool** |  | 
**approved** | **bool** |  | 
**created_date** | **datetime** |  | 
**last_update** | **datetime** |  | 
**travel_agent** | [**TravelAgentSupplier**](TravelAgentSupplier.md) |  | 
**owner_image_id** | **str** | The company image ID | 
**online_presence** | [**List[OnlinePresenceSupplier]**](OnlinePresenceSupplier.md) |  | [optional] 
**annual_travel_spend_in_dollars** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.display_company_supplier import DisplayCompanySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayCompanySupplier from a JSON string
display_company_supplier_instance = DisplayCompanySupplier.from_json(json)
# print the JSON string representation of the object
print(DisplayCompanySupplier.to_json())

# convert the object into a dict
display_company_supplier_dict = display_company_supplier_instance.to_dict()
# create an instance of DisplayCompanySupplier from a dict
display_company_supplier_from_dict = DisplayCompanySupplier.from_dict(display_company_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


