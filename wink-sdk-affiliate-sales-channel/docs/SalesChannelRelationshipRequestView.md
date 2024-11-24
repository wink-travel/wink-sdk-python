# SalesChannelRelationshipRequestView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user** | [**SalesChannelRelationshipRequest**](SalesChannelRelationshipRequest.md) |  | [optional] 
**request** | [**SalesChannelRelationshipRequest**](SalesChannelRelationshipRequest.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.sales_channel_relationship_request_view import SalesChannelRelationshipRequestView

# TODO update the JSON string below
json = "{}"
# create an instance of SalesChannelRelationshipRequestView from a JSON string
sales_channel_relationship_request_view_instance = SalesChannelRelationshipRequestView.from_json(json)
# print the JSON string representation of the object
print(SalesChannelRelationshipRequestView.to_json())

# convert the object into a dict
sales_channel_relationship_request_view_dict = sales_channel_relationship_request_view_instance.to_dict()
# create an instance of SalesChannelRelationshipRequestView from a dict
sales_channel_relationship_request_view_from_dict = SalesChannelRelationshipRequestView.from_dict(sales_channel_relationship_request_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


