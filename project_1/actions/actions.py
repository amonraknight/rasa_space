# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# This is a simple example for a custom action which utters "Hello World!"

#
#
# class ActionHelloWorld(Action):
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

class ActionNifiCreateProcessor(Action):
	
	def name(self) -> Text:
		return 'action_nifi_create_processor'
	
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		'''
		There are 3 slots now:
		  current_processor_type
		  current_processor_name
		  upstream_processor_name
		'''
		
		current_processor_type = tracker.get_slot('current_processor_type')
		current_processor_name = tracker.get_slot('current_processor_name')
		upstream_processor_name = tracker.get_slot('upstream_processor_name')
		
		dispatcher.utter_message(text='OK. I\'m to create the %s processor \'%s\' following %s.'% 
		(current_processor_type, current_processor_name, upstream_processor_name))
		
		return []