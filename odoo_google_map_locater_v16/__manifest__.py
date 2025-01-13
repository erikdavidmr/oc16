{
    "name": "Google Map Locator",
    "description": """The Google Map Locator app enhances user experience by integrating the Google Maps API to provide seamless address input functionality. Users can type in their desired addresses, with real-time auto-completion suggestions powered by the Google Places API, which helps them find the correct locations quickly and accurately. Once an address is selected, 
    it is displayed on an embedded Google Map for visual confirmation, allowing users to interact with the map by zooming in and out or dragging it to explore surrounding areas. The app also employs geocoding to convert addresses into geographic coordinates for precise location tracking, while reverse geocoding allows users to obtain addresses by clicking on specific map locations. Additionally, robust error handling ensures that only valid addresses are accepted, further streamlining the user experience.
 """,
    "summary": "The Google Map Locator app enables users to easily input addresses by integrating Google Maps through the Google API. It allows users to enter an address, automatically display the location on a map, and auto-populate related address fields such as country, state, and city. This integration streamlines address input and improves accuracy by using real-time data from Google Maps, ensuring a smooth and efficient user experience.",
    "category": "Services",
    "version": "16.0.1.0.0",
    "author": "Zehntech Technologies Inc.",
    "company": "Zehntech Technologies Inc.",
    "maintainer": "Zehntech Technologies Inc.",
    "contributor": "Zehntech Technologies Inc.",
    "website": "https://www.zehntech.com/",
    "support": "odoo-support@zehntech.com",
    "depends": ['base', 'contacts', 'crm'],
    "data":[
        'views/res_partner_views.xml',    
        'views/res_config_settings_views.xml',
        'views/crm_lead_views.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo-google-map-locater-v16/static/src/js/map_widget.js',  
            'odoo-google-map-locater-v16/static/src/xml/odoo-google-map-locater-v16_widget.xml',   
            'odoo-google-map-locater-v16/static/src/css/style.css',     
        ],
    },
    'images': ['static/description/banner.png'],
    "license": "OPL-1",
    "installable": True,
    "application": True,
    "auto_install": False,
    "price": 00.00,
    "currency": "USD",
}