# SyndicationSettingsWithThemeColorsAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**user_identifier** | **str** | Creator of entry | 
**owner_identifier** | **str** | The user&#39;s owner company this entry associates with | 
**item_display** | **str** | Whether to treat all links as flat web links or try to embed more advanced data. | [optional] 
**customization_identifier** | **str** | Customization identifier | 
**layout_display** | **str** | Which way to itemDisplay the list when WinkLinks first loads | [optional] [default to 'GRID_COLUMNS']
**profile_picture_geometry** | **str** | Controls how to itemDisplay profile picture | [optional] [default to 'CIRCLE']
**online_presence_position** | **str** | Where to show the online presence icons | [optional] [default to 'TOP']
**qr_code_options** | [**SyndicationSettingsQrCodeOptionsAffiliate**](SyndicationSettingsQrCodeOptionsAffiliate.md) | Customizable QR code options | [optional] 
**theme_colors** | [**CustomizationThemeColorsAffiliate**](CustomizationThemeColorsAffiliate.md) | Theme colors are connected with the primary account customization. | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.syndication_settings_with_theme_colors_affiliate import SyndicationSettingsWithThemeColorsAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SyndicationSettingsWithThemeColorsAffiliate from a JSON string
syndication_settings_with_theme_colors_affiliate_instance = SyndicationSettingsWithThemeColorsAffiliate.from_json(json)
# print the JSON string representation of the object
print(SyndicationSettingsWithThemeColorsAffiliate.to_json())

# convert the object into a dict
syndication_settings_with_theme_colors_affiliate_dict = syndication_settings_with_theme_colors_affiliate_instance.to_dict()
# create an instance of SyndicationSettingsWithThemeColorsAffiliate from a dict
syndication_settings_with_theme_colors_affiliate_from_dict = SyndicationSettingsWithThemeColorsAffiliate.from_dict(syndication_settings_with_theme_colors_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


