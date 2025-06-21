# UpsertContactInfoRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservations_contact** | [**ContactSupplier**](ContactSupplier.md) | [Online] reservationsContact desk assistant at property that can be contacted by travelers and agents. | 
**revenue_contact** | [**ContactSupplier**](ContactSupplier.md) | Digital revenueContact mgmt team at property that can be contacted by Wink. | 
**marketing_contact** | [**ContactSupplier**](ContactSupplier.md) | Marketing team at property that can be contacted by Wink. | 
**reservation_desk_start_time** | **str** | If the reservationsContact desk does not operate 24 hours, enter a start time. | 
**reservation_desk_end_time** | **str** | If the reservationsContact desk does not operate 24 hours, enter an end time. | 

## Example

```python
from wink_sdk_extranet_property.models.upsert_contact_info_request_supplier import UpsertContactInfoRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertContactInfoRequestSupplier from a JSON string
upsert_contact_info_request_supplier_instance = UpsertContactInfoRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertContactInfoRequestSupplier.to_json())

# convert the object into a dict
upsert_contact_info_request_supplier_dict = upsert_contact_info_request_supplier_instance.to_dict()
# create an instance of UpsertContactInfoRequestSupplier from a dict
upsert_contact_info_request_supplier_from_dict = UpsertContactInfoRequestSupplier.from_dict(upsert_contact_info_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


