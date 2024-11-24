# SupplierLeadSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) |  | 
**owner** | [**KeyValuePairSupplier**](KeyValuePairSupplier.md) |  | [optional] 
**status** | **str** | Lead status | 
**place_id** | **str** | Unique ID | 
**name_in_english** | **str** | Name of lead | 
**name_in_local_language** | **str** | Name of lead in local language | [optional] 
**google_maps_url** | **str** | Google Maps URL of the place | 
**phone** | **str** | Telephone of lead | [optional] 
**address** | [**AddressSupplier**](AddressSupplier.md) |  | [optional] 
**address_local** | [**SimpleAddressSupplier**](SimpleAddressSupplier.md) |  | [optional] 
**formatted_address** | **str** | Formatted address in English | [optional] 
**formatted_address_local** | **str** | Formatted address in local language if available | [optional] 
**html_address** | **str** | Html address in English | [optional] 
**html_address_local** | **str** | Html address in local language if available | [optional] 
**location** | [**GeoJsonPointSupplier**](GeoJsonPointSupplier.md) |  | 
**photos** | [**List[SimpleMultimediaSupplier]**](SimpleMultimediaSupplier.md) | Photos for property | [optional] 
**rating** | **float** | Hotel rating | [optional] 
**user_rating_total** | **int** | Total umber of user ratings | [optional] 
**utc_offset_minutes** | **int** | UTC offset minutes | 
**website** | **str** | Website | [optional] 
**message_from_user** | **str** | A personalized message from the inviter | [optional] 
**city_options** | [**List[GeoNameSupplier]**](GeoNameSupplier.md) |  | [optional] 
**descriptions** | [**List[SimpleDescriptionSupplier]**](SimpleDescriptionSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.supplier_lead_supplier import SupplierLeadSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierLeadSupplier from a JSON string
supplier_lead_supplier_instance = SupplierLeadSupplier.from_json(json)
# print the JSON string representation of the object
print(SupplierLeadSupplier.to_json())

# convert the object into a dict
supplier_lead_supplier_dict = supplier_lead_supplier_instance.to_dict()
# create an instance of SupplierLeadSupplier from a dict
supplier_lead_supplier_from_dict = SupplierLeadSupplier.from_dict(supplier_lead_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


