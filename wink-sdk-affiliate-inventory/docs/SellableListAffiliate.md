# SellableListAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**owner_identifier** | **UUID** | AffiliateAccount identifier | 
**name** | **str** | Descriptive name of this list for seller use only | 
**customization_identifier** | **UUID** | Customization identifier | 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Contains custom title and description of grid | 
**keywords** | **List[str]** | Keywords is meta data for the grid you created that can be used for SEO purposes. | 
**status** | **str** | Status | [default to 'ACTIVE']
**list_type** | **str** | List type | 
**list_identifier** | **UUID** | Depending on the &#x60;listType&#x60;, this is either the list / search / channel inventory identifier. | 
**animate** | **bool** | Create an animated gif instead of a list of images | [optional] [default to False]
**animate_delay** | **int** | Controls animation delay in milliseconds. -1 is disabled | [optional] [default to -1]
**sort** | **str** | Determines which badge to show on the Web Component. Is also used to sort properties for search grids. | [optional] 
**display_type** | **str** | Indicate which initial values to display first on the front-facing card | [default to 'NATIVE']

## Example

```python
from wink_sdk_affiliate_inventory.models.sellable_list_affiliate import SellableListAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SellableListAffiliate from a JSON string
sellable_list_affiliate_instance = SellableListAffiliate.from_json(json)
# print the JSON string representation of the object
print(SellableListAffiliate.to_json())

# convert the object into a dict
sellable_list_affiliate_dict = sellable_list_affiliate_instance.to_dict()
# create an instance of SellableListAffiliate from a dict
sellable_list_affiliate_from_dict = SellableListAffiliate.from_dict(sellable_list_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


