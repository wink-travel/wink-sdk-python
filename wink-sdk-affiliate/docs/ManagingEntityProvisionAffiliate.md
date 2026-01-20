# ManagingEntityProvisionAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Stripe subscription ID | 
**invoice_id** | **str** | Latest Stripe invoice ID | 
**customer_id** | **str** | Stripe customer ID | 
**customer_email** | **str** | Stripe customer ID | 
**customer_phone** | **str** | Stripe customer ID | 
**price_lookup_key** | **str** | Stripe price lookup key | 
**status** | **str** | Stripe subscription status | 
**invoice_status** | **str** | Stripe latest invoice status | 
**created_at** | **datetime** | Time subscription was created | 
**updated_at** | **datetime** | Time subscription was last updated | 
**canceled_at** | **datetime** | Time subscription was canceled | 
**trial_expires** | **datetime** | Time subscription was last updated | 
**metadata** | **Dict[str, str]** | Optional information we receive from Stripe that we want to save. | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.managing_entity_provision_affiliate import ManagingEntityProvisionAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ManagingEntityProvisionAffiliate from a JSON string
managing_entity_provision_affiliate_instance = ManagingEntityProvisionAffiliate.from_json(json)
# print the JSON string representation of the object
print(ManagingEntityProvisionAffiliate.to_json())

# convert the object into a dict
managing_entity_provision_affiliate_dict = managing_entity_provision_affiliate_instance.to_dict()
# create an instance of ManagingEntityProvisionAffiliate from a dict
managing_entity_provision_affiliate_from_dict = ManagingEntityProvisionAffiliate.from_dict(managing_entity_provision_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


