# EngineClientNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique engine configuration identifier | [optional] 
**name** | **str** | Engine configuration name | 
**append_to_page_title** | **str** | Whether to append text to the existing booking engine page title. | [optional] 
**owner_identifier** | **str** | Engine configuration record creator identifier | [optional] 
**owner_name** | **str** | Name of company owner. | [optional] 
**sub_type** | **str** | Sales channel sub-type. | [optional] 
**primary** | **bool** | Indicates whether this configuration is primary. A primary configuration cannot be removed. | [optional] [default to False]
**google_analytics_measurement_id** | **str** | If you want to track analytics with Google Analytics and GTM for your self-hosted booking engine, you need to import our [GTM profile](https://www.dropbox.com/s/o6rwluclvsgydma/gtm-template-2020-2.json?dl&#x3D;0) into your GTM container and link it with your Google Analytics account. [More about that here](https://bearchoke.atlassian.net/wiki/spaces/TC/pages/2941648897/Linking+your+Google+Tag+Manager+account)  | [optional] 
**google_maps_api_key** | **str** | If you want your users to see Google Maps in your hosted booking engine, go to [Google Maps](https://console.developers.google.com/projectselector2/apis/credentials?supportedpurview&#x3D;project) and create an API key for your site. | [optional] 
**default_currency** | **str** | Control which currency your users see prices in initially. | [optional] [default to 'USD']
**default_language** | **str** | Control which language your users see text in initially. | [optional] [default to 'en']
**logo_image_identifier** | **str** | Customize booking confirmation emails by adding a custom logo to your configuration. | [optional] 
**hosted_booking_engine_url** | **str** | If you are self-hosting our booking engine, let us know where it is hosted. Note: This url needs to be secured with SSL. | [optional] [default to 'https://ota.wink.travel']
**self_hosted** | **bool** | Flag to indicate you are self-hosting our booking engine and not using our default booking engine url. | [optional] [default to False]
**theme_colors** | [**EngineConfigurationThemeColorsNonAuthenticatedEntity**](EngineConfigurationThemeColorsNonAuthenticatedEntity.md) |  | [optional] 
**number_of_advance_days** | **int** | You can control the initial itinerary date used to retrieve travel blocking prices. You can do it in one of two ways: 1. Dynamically set the date by indicating how long and how many days in advance (this field), of today&#39;s date, you want to display prices for. 2. Set a fixed date to display prices for. Option 1 is the most shared. Option 2 is for when you want to create a new customization and apply it to a specific event that occurs on a specific date. If you don&#39;t use either of these options, the itinerary will default to today&#39;s date with one night stay. ONLY populate this field if you want to control the itinerary date. Also, leave &#x60;startDate&#x60; and &#x60;endDate&#x60; empty. | [optional] 
**number_of_stay_days** | **int** | You can control the initial itinerary date used to retrieve travel blocking prices. You can do it in one of two ways: 1. Dynamically set the date by indicating how long (this field) and how many days in advance, of today&#39;s date, you want to display prices for. 2. Set a fixed date to display prices for. Option 1 is the most shared. Option 2 is for when you want to create a new customization and apply it to a specific event that occurs on a specific date. If you don&#39;t use either of these options, the itinerary will default to today&#39;s date with one night stay. ONLY populate this field if you want to control the itinerary date. Also, leave &#x60;startDate&#x60; and &#x60;endDate&#x60; empty. | [optional] 
**start_date** | **date** | Set a fixed itinerary start date. ONLY populate this field if you want to fix the itinerary date. Also, leave &#x60;numberOfAdvanceDays&#x60; and &#x60;numberOfStayDays&#x60; empty. | [optional] 
**end_date** | **date** | Set a fixed itinerary end date ONLY populate this field if you want to fix the itinerary date. Also, leave &#x60;numberOfAdvanceDays&#x60; and &#x60;numberOfStayDays&#x60; empty. | [optional] 
**room_configurations** | [**List[RoomConfigurationNonAuthenticatedEntity]**](RoomConfigurationNonAuthenticatedEntity.md) | Control how many adults / children will be staying and how many rooms. Defaults to: One room, two adults. | [optional] 
**use_days** | **bool** | if true, we use numberOfAdvanceDays / numberOfStayDays properties - false, we use startDate / endDate | [optional] 
**promotional_codes** | **List[str]** | If you&#39;ve received special promotional codes from suppliers to give to your audience, you can choose to bake these code directly into the price by entering them here. | [optional] 
**wc_book_click_action** | **str** | Action to complete once a user clicks on the CTA button on blocking. | [optional] 
**show_unavailable_card** | **bool** | Show unavailable blocking card when blocking not currently for sale. Otherwise, it displays a normal card but without the price. | [optional] 
**show_rankings** | **bool** | Whether to display rankings (lifestyle, eco score and reviews) on hotel landing page. | [optional] 
**layout** | **str** | Choose how you want our web component cards laid out. | [optional] [default to 'INFORMATIONAL']
**card_layout** | **str** | Choose how you large you want our web component cards to be. | [optional] [default to 'VERTICAL']

## Example

```python
from wink_sdk_engine_client.models.engine_client_non_authenticated_entity import EngineClientNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EngineClientNonAuthenticatedEntity from a JSON string
engine_client_non_authenticated_entity_instance = EngineClientNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(EngineClientNonAuthenticatedEntity.to_json())

# convert the object into a dict
engine_client_non_authenticated_entity_dict = engine_client_non_authenticated_entity_instance.to_dict()
# create an instance of EngineClientNonAuthenticatedEntity from a dict
engine_client_non_authenticated_entity_from_dict = EngineClientNonAuthenticatedEntity.from_dict(engine_client_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


