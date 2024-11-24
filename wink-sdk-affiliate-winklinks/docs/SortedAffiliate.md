# SortedAffiliate

Sorted object strictly to use for sorting of list items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | List item ID | 
**index** | **int** | List item position | 

## Example

```python
from wink_sdk_affiliate_winklinks.models.sorted_affiliate import SortedAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SortedAffiliate from a JSON string
sorted_affiliate_instance = SortedAffiliate.from_json(json)
# print the JSON string representation of the object
print(SortedAffiliate.to_json())

# convert the object into a dict
sorted_affiliate_dict = sorted_affiliate_instance.to_dict()
# create an instance of SortedAffiliate from a dict
sorted_affiliate_from_dict = SortedAffiliate.from_dict(sorted_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


