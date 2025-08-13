# UpsertSyndicationSettingsAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_display** | **str** | Whether to treat all links as flat web links or try to embed more advanced data. | 
**customization_identifier** | **str** | Customization identifier | 
**layout_display** | **str** | Which way to display the list when WinkLinks first loads | [optional] [default to 'GRID_COLUMNS']
**profile_picture_geometry** | **str** | Controls how to display profile picture | [optional] [default to 'CIRCLE']
**online_presence_position** | **str** | Where to show the online presence icons | [optional] [default to 'TOP']
**theme_colors** | [**CustomizationThemeColorsAffiliate**](CustomizationThemeColorsAffiliate.md) | Theme colors are connected with the primary account customization. | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.upsert_syndication_settings_affiliate import UpsertSyndicationSettingsAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSyndicationSettingsAffiliate from a JSON string
upsert_syndication_settings_affiliate_instance = UpsertSyndicationSettingsAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertSyndicationSettingsAffiliate.to_json())

# convert the object into a dict
upsert_syndication_settings_affiliate_dict = upsert_syndication_settings_affiliate_instance.to_dict()
# create an instance of UpsertSyndicationSettingsAffiliate from a dict
upsert_syndication_settings_affiliate_from_dict = UpsertSyndicationSettingsAffiliate.from_dict(upsert_syndication_settings_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


