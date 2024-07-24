from pydantic import Enum


class CommunicationMethod(Enum):
    TELEGRAM = "TELEGRAM",
    PHONE = "PHONE",
    WHATSAPP = "WHATSAPP"