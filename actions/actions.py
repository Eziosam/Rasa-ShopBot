# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

path_to_db = "actions/example.db"


# class ActionProductSearch(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
path_to_db = "actions/example.db"
class ActionProductSearch(Action):

    def name(self) -> Text:
        return "action_product_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        shoe= [tracker.latest_message['entities'][0]['value']]

        cursor.execute("SELECT pname FROM inventory WHERE pname=? ", shoe)
        data_row = cursor.fetchone()

        if data_row:
          dispatcher.utter_message(text="Found!")
          dispatcher.utter_message(image='https://i.ibb.co/3c3jQNR/product-1.png') 
                        
        else:
          dispatcher.utter_message(text="Not Available!")  

class ActionProductPriceSearch(Action):

    def name(self) -> Text:
        return "action_product_price_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        pname= [tracker.latest_message['entities'][0]['value']]

        cursor.execute("SELECT price FROM inventory WHERE pname=? ", pname)
        data_row = cursor.fetchone()

        if data_row:
          dispatcher.utter_message("Price of "+ str(pname[0]) +" is "+str(data_row[0]))
        else:
          dispatcher.utter_message(text="Not Available!")  

class ActionProductQuantitySearch(Action):

    def name(self) -> Text:
        return "action_product_quantity_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        pname= [tracker.latest_message['entities'][0]['value']]

        cursor.execute("SELECT amount FROM inventory WHERE pname=? ", pname)
        data_row = cursor.fetchone()

        if data_row:
          dispatcher.utter_message("We currently  have "+str(data_row[0]) +" units of " + str(pname[0]))
        else:
          dispatcher.utter_message(text="Not Available!") 

class ActionProductDeliveryFeeSearch(Action):

    def name(self) -> Text:
        return "action_fetch_del_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        address= [tracker.latest_message['entities'][0]['value']]

        cursor.execute("SELECT Fee FROM Delivery WHERE address=? ", address)
        data_row = cursor.fetchone()

        if data_row:
          dispatcher.utter_message("Sir ,The Delivery fee is "+str(data_row[0]) +" USD$ " )
        else:
          dispatcher.utter_message(text="Not Available!") 



class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_carousels"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        
        
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        pname= ["apple"]

        cursor.execute("SELECT price FROM inventory WHERE pname=? ", pname)
        data_row = cursor.fetchone()

        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Sony Bravia TV",
                        "subtitle": data_row[0],
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/Television/sony/KDL%20W600D-500x500.jpg",
                        "buttons": [ 
                            {
                            "title": "Add to Cart",
                            "payload": "Happy",
                            "type": "postback"
                            },
                            {
                            "title": "Show More",
                            "payload": "sad",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Samsung 870 EVO SSD",
                        "subtitle": "$12",
                        "image_url": "https://www.startech.com.bd/image/cache/catalog/ssd/samsung/870-evo/870-evo-01-500x500.jpg",
                        
                        "buttons": [ 
                            {
                            "title": "Buy",
                            "url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
                            "type": "web_url"
                            }
                        ]
                    },
                          {
                        "title": "Core i7 CPU",
                        "subtitle": "$12,000",
                        "image_url": "https://i.imgur.com/UfDtQuv.jpeg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
                            "type": "web_url"
                            }
                            ]
                        }
                   ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []
