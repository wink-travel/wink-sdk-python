# UpgradeView

FormattedAncillary blocking to ancillary a room booking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**upgrade** | [**AddOn**](AddOn.md) |  | [optional] 
**featured_image_identifier** | **str** | Convenience method to easily access the featured image without having to go through the entire list of images. Defaults to placeholder image if no image is present. | [optional] [default to 'noimage_opaque_nyrtl0.png']

## Example

```python
from wink_sdk_extranet_monetize.models.upgrade_view import UpgradeView

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeView from a JSON string
upgrade_view_instance = UpgradeView.from_json(json)
# print the JSON string representation of the object
print(UpgradeView.to_json())

# convert the object into a dict
upgrade_view_dict = upgrade_view_instance.to_dict()
# create an instance of UpgradeView from a dict
upgrade_view_from_dict = UpgradeView.from_dict(upgrade_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


