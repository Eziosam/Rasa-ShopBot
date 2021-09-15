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

        cursor.execute("SELECT * FROM inventory WHERE pname=? ", shoe)
        data_row = cursor.fetchone()

        if data_row:
          dispatcher.utter_message(text="Found!")
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
        

