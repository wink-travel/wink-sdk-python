# StateAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of records to be skipped by the pager. | [optional] [default to 0]
**take** | **int** | Number of records to take. | [optional] [default to 30]
**sort** | [**List[SortDescriptorAffiliate]**](SortDescriptorAffiliate.md) | Descriptors used for sorting result set. | [optional] 
**filter** | [**CompositeFilterDescriptorAffiliate**](CompositeFilterDescriptorAffiliate.md) |  | [optional] 
**group** | [**List[GroupDescriptorAffiliate]**](GroupDescriptorAffiliate.md) | Descriptors to group result sets by. | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.state_affiliate import StateAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of StateAffiliate from a JSON string
state_affiliate_instance = StateAffiliate.from_json(json)
# print the JSON string representation of the object
print(StateAffiliate.to_json())

# convert the object into a dict
state_affiliate_dict = state_affiliate_instance.to_dict()
# create an instance of StateAffiliate from a dict
state_affiliate_from_dict = StateAffiliate.from_dict(state_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


