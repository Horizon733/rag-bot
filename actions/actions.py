import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action

from rag.query_rag import query_rag

logger = logging.getLogger(__name__)


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        response = query_rag(tracker.latest_message)
        logger.debug(f"response: {response}")
        dispatcher.utter_message(text=response)

        return []