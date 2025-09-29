# SupplierLeadAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user** | [**KeyValuePairAffiliate**](KeyValuePairAffiliate.md) | The user who initiated the creation of this object. Contains userId as value and username as label. | 
**owner** | [**KeyValuePairAffiliate**](KeyValuePairAffiliate.md) | Usually the company account ID that the lead occurred under. Contains company ID as value and company name as label. | [optional] 
**status** | **str** | Lead status | 
**place_id** | **str** | Unique ID | 
**name_in_english** | **str** | Name of lead | 
**name_in_local_language** | **str** | Name of lead in local language | [optional] 
**google_maps_url** | **str** | Google Maps URL of the place | 
**phone** | **str** | Telephone of lead | [optional] 
**address** | [**AddressAffiliate**](AddressAffiliate.md) | Address in English | [optional] 
**address_local** | [**SimpleAddressAffiliate**](SimpleAddressAffiliate.md) | Address in local language if available | [optional] 
**formatted_address** | **str** | Formatted address in English | [optional] 
**formatted_address_local** | **str** | Formatted address in local language if available | [optional] 
**html_address** | **str** | Html address in English | [optional] 
**html_address_local** | **str** | Html address in local language if available | [optional] 
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Country | 
**photos** | [**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md) | Photos for property | [optional] 
**rating** | **float** | Hotel rating | [optional] 
**user_rating_total** | **int** | Total umber of user ratings | [optional] 
**utc_offset_minutes** | **int** | UTC offset minutes | 
**website** | **str** | Website | [optional] 
**message_from_user** | **str** | A personalized message from the inviter | [optional] 
**city_options** | **List[object]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.supplier_lead_affiliate import SupplierLeadAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierLeadAffiliate from a JSON string
supplier_lead_affiliate_instance = SupplierLeadAffiliate.from_json(json)
# print the JSON string representation of the object
print(SupplierLeadAffiliate.to_json())

# convert the object into a dict
supplier_lead_affiliate_dict = supplier_lead_affiliate_instance.to_dict()
# create an instance of SupplierLeadAffiliate from a dict
supplier_lead_affiliate_from_dict = SupplierLeadAffiliate.from_dict(supplier_lead_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


