"""
Module for Watson translation
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def english_to_french(text):
    """
    Function that receive english text and return french text
    """
    if text is None:
        return None
    translation = language_translator.translate(text=text,model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]


def french_to_english(text):
    """
    Function that receive french text and return english text
    """
    if text is None:
        return None
    translation = language_translator.translate(text=text,model_id='fr-en').get_result()
    # print("translation:",translation)
    return translation["translations"][0]["translation"]
    