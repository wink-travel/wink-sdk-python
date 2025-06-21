# NotificationAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**owner_identifier** | **str** | Owner identifier | 
**priority** | **str** | Importance of message | 
**type** | **str** | Message type | 
**recipient_type** | **str** | Recipient type | 
**application** | **str** | Application domain | 
**message_template_id** | **str** | Message template | 
**subject** | **str** | Subject of message | 
**body** | **str** | Subject of message | 
**cta_url** | **str** | Path to feature | 
**read** | **bool** | AffiliateAccountLightweight read announcement | [optional] 
**marked_as_removed** | **bool** | Message marked as removed | [optional] 
**notify_via_email** | **bool** | Also send email announcement | [optional] 

## Example

```python
from wink_sdk_notification.models.notification_affiliate import NotificationAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationAffiliate from a JSON string
notification_affiliate_instance = NotificationAffiliate.from_json(json)
# print the JSON string representation of the object
print(NotificationAffiliate.to_json())

# convert the object into a dict
notification_affiliate_dict = notification_affiliate_instance.to_dict()
# create an instance of NotificationAffiliate from a dict
notification_affiliate_from_dict = NotificationAffiliate.from_dict(notification_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


