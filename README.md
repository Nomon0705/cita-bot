#this is the Readme file
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class CustomerProfile:
    anticaptcha_api_key: Optional[str] = None
    auto_captcha: bool = True
    auto_office: bool = True
    chrome_driver_path: Optional[str] = None
    min_date: Optional[str] = None  # format: "dd/mm/yyyy"
    max_date: Optional[str] = None  # format: "dd/mm/yyyy"
    save_artifacts: bool = False
    sms_webhook_token: Optional[str] = None
    wait_exact_time: Optional[List[List[int]]] = field(default_factory=list)  # [[minute, second]]

    province: Province = Province.BARCELONA
    operation_code: OperationType = OperationType.TOMA_HUELLAS
    doc_type: DocType = None
    doc_value: str = ""
    name: str = ""
    country: str = "RUSIA"
    year_of_birth: Optional[str] = None
    phone: str = ""
    email: str = ""
    offices: List[str] = field(default_factory=list)
    except_offices: List[str] = field(default_factory=list)
    reason_or_type: str = "solicitud de asilo"
