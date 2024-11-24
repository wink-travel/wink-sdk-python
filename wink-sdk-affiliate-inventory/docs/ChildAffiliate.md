# ChildAffiliate

BookingItineraryRoomConfigurationChild configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_affiliate_inventory.models.child_affiliate import ChildAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ChildAffiliate from a JSON string
child_affiliate_instance = ChildAffiliate.from_json(json)
# print the JSON string representation of the object
print(ChildAffiliate.to_json())

# convert the object into a dict
child_affiliate_dict = child_affiliate_instance.to_dict()
# create an instance of ChildAffiliate from a dict
child_affiliate_from_dict = ChildAffiliate.from_dict(child_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


