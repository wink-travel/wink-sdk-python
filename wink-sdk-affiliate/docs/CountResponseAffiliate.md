# CountResponseAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True if count query worked. | 
**count** | **int** | Number of reviews for this property. | 

## Example

```python
from wink_sdk_affiliate.models.count_response_affiliate import CountResponseAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CountResponseAffiliate from a JSON string
count_response_affiliate_instance = CountResponseAffiliate.from_json(json)
# print the JSON string representation of the object
print(CountResponseAffiliate.to_json())

# convert the object into a dict
count_response_affiliate_dict = count_response_affiliate_instance.to_dict()
# create an instance of CountResponseAffiliate from a dict
count_response_affiliate_from_dict = CountResponseAffiliate.from_dict(count_response_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


