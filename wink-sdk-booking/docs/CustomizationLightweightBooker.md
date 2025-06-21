# CustomizationLightweightBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique customization configuration identifier | 
**name** | **str** | Engine configuration name | 
**user_identifier** | **str** | Authenticated user identifier | 
**owner_identifier** | **str** | Engine configuration record creator identifier | 
**owner_name** | **str** | Name of company owner. | 
**sub_type** | **str** | Sales channel sub-type. | 
**default_currency** | **str** | Control which currency your users see prices in initially. | [optional] [default to 'USD']
**default_language** | **str** | Control which language your users see text in initially. | [optional] [default to 'en']
**default_lifestyle** | **str** | Control which lifestyle contextx your users see initially. | [optional] 
**logos** | [**List[SimpleMultimediaBooker]**](SimpleMultimediaBooker.md) | Customize booking confirmation emails by adding a custom logo to your configuration. | [optional] 
**hosted_booking_engine_url** | **str** | If you are self-hosting our booking customization, let us know where it is hosted. Note: This url needs to be secured with SSL. | [optional] [default to 'https://ota.wink.travel']
**self_hosted** | **bool** | Flag to indicate you are self-hosting our booking customization and not using our default booking customization url. | [optional] [default to False]
**theme_colors** | [**CustomizationThemeColorsBooker**](CustomizationThemeColorsBooker.md) | Choose how you want our web components to look and more closely match with your own site style. | [optional] 
**card_layout** | **str** | Choose how you large you want our web component cards to be. | [optional] [default to 'VERTICAL']
**layout** | **str** | Choose how you want our web component cards laid out. | [optional] [default to 'INFORMATIONAL']
**card_design** | **str** | Choose the card design to use on our web component cards. | [optional] [default to 'DEFAULT']
**number_of_advance_days** | **int** | You can control the initial itinerary date used to retrieve travel blocking prices. You can do it in one of two ways: 1. Dynamically set the date by indicating how long and how many days in advance (this field), of today&#39;s date, you want to display prices for. 2. Set a fixed date to display prices for. Option 1 is the most shared. Option 2 is for when you want to create a new customization and apply it to a specific event that occurs on a specific date. If you don&#39;t use either of these options, the itinerary will default to today&#39;s date with one night stay. ONLY populate this field if you want to control the itinerary date. Also, leave &#x60;startDate&#x60; and &#x60;endDate&#x60; empty. | [optional] 
**number_of_stay_days** | **int** | You can control the initial itinerary date used to retrieve travel blocking prices. You can do it in one of two ways: 1. Dynamically set the date by indicating how long (this field) and how many days in advance, of today&#39;s date, you want to display prices for. 2. Set a fixed date to display prices for. Option 1 is the most shared. Option 2 is for when you want to create a new customization and apply it to a specific event that occurs on a specific date. If you don&#39;t use either of these options, the itinerary will default to today&#39;s date with one night stay. ONLY populate this field if you want to control the itinerary date. Also, leave &#x60;startDate&#x60; and &#x60;endDate&#x60; empty. | [optional] 
**start_date** | **date** | Set a fixed itinerary start date. ONLY populate this field if you want to fix the itinerary date. Also, leave &#x60;numberOfAdvanceDays&#x60; and &#x60;numberOfStayDays&#x60; empty. | [optional] 
**end_date** | **date** | Set a fixed itinerary end date ONLY populate this field if you want to fix the itinerary date. Also, leave &#x60;numberOfAdvanceDays&#x60; and &#x60;numberOfStayDays&#x60; empty. | [optional] 
**room_configurations** | [**List[RoomConfigurationBooker]**](RoomConfigurationBooker.md) | Control how many adults / children will be staying and how many rooms. Defaults to: One room, two adults. | [optional] 
**use_days** | **bool** | if true, we use numberOfAdvanceDays / numberOfStayDays properties - false, we use startDate / endDate | [optional] 
**promotional_codes** | **List[str]** | If you&#39;ve received special promotional codes from suppliers to give to your audience, you can choose to bake these code directly into the price by entering them here. | [optional] 
**send_booking_notification_emails_to_property** | **bool** | An integrator can choose to disable outgoing emails to properties because they want to do that themselves. | [optional] [default to True]
**send_booking_notification_emails_to_booker** | **bool** | An integrator can choose to disable outgoing emails to users because they want to do that themselves. | [optional] [default to True]
**send_booking_notification_emails_to_channel_manager** | **bool** | An integrator can choose to disable notifying the property&#39;s channel manager. Note: This should ONLY be done for testing. | [optional] [default to True]
**wc_book_click_action** | **str** | Action to complete once a user clicks on the CTA button on blocking. | [optional] 
**city** | [**GeoNameLightweightBooker**](GeoNameLightweightBooker.md) |  | [optional] 
**show_unavailable_card** | **bool** | Show unavailable blocking card when blocking not currently for sale. Otherwise, it displays a normal card but without the price. | [optional] 
**show_rankings** | **bool** | Whether to display rankings (lifestyle, eco score and reviews) on hotel landing page. | [optional] 
**show_search** | **bool** | This feature flag controls whether to let a user move away from the hotel landing page using search. | [optional] 

## Example

```python
from wink_sdk_booking.models.customization_lightweight_booker import CustomizationLightweightBooker

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationLightweightBooker from a JSON string
customization_lightweight_booker_instance = CustomizationLightweightBooker.from_json(json)
# print the JSON string representation of the object
print(CustomizationLightweightBooker.to_json())

# convert the object into a dict
customization_lightweight_booker_dict = customization_lightweight_booker_instance.to_dict()
# create an instance of CustomizationLightweightBooker from a dict
customization_lightweight_booker_from_dict = CustomizationLightweightBooker.from_dict(customization_lightweight_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


