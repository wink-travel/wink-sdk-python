# AffiliateAccountSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **str** | User or Registered client owner identifier that created this record | 
**owner** | [**AffiliateAccountUserSupplier**](AffiliateAccountUserSupplier.md) | Owner | 
**name** | **str** | Name of company | 
**url_name** | **str** | Url slug of company name | 
**unique_id** | **str** | Even shorter url identifier | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**enabled** | **bool** | Whether this company is enabled by platform. | 
**approved** | **bool** | Whether this company has been approved by KYC. | [default to False]
**company_type** | **str** | Type of company | 
**type** | **str** | Type of sales channel | 
**description** | **str** | Account description. | [optional] 
**address** | [**AddressSupplier**](AddressSupplier.md) |  | 
**managers** | [**List[AffiliateAccountUserSupplier]**](AffiliateAccountUserSupplier.md) |  | [optional] 
**logo** | [**SimpleMultimediaSupplier**](SimpleMultimediaSupplier.md) | Customize account with a custom logo / profile picture. | [optional] 
**travel_agent** | [**TravelAgentSupplier**](TravelAgentSupplier.md) | Customize account with a custom logo / profile picture. | [optional] 
**managed_by** | [**ManagedByEntitySupplier**](ManagedByEntitySupplier.md) | If another company entity is managing this property, on behalf of the property, it can be specified here and the managing entity would be applicable a management fee on every booking. | [optional] 
**online_presence** | **List[object]** |  | [optional] 
**annual_travel_spend_in_dollars** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | How much user or company spends on travel per year. | [optional] 
**plans** | **List[object]** |  | [optional] 
**previous_url_name_list** | **List[object]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.affiliate_account_supplier import AffiliateAccountSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateAccountSupplier from a JSON string
affiliate_account_supplier_instance = AffiliateAccountSupplier.from_json(json)
# print the JSON string representation of the object
print(AffiliateAccountSupplier.to_json())

# convert the object into a dict
affiliate_account_supplier_dict = affiliate_account_supplier_instance.to_dict()
# create an instance of AffiliateAccountSupplier from a dict
affiliate_account_supplier_from_dict = AffiliateAccountSupplier.from_dict(affiliate_account_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


