@dataclass
class CustomerProfile:
    anticaptcha_api_key: Optional[str] = None
    auto_captcha: bool = True
    auto_office: bool = True
    chrome_driver_path: str = None
    min_date: Optional[str] = None  # "dd/mm/yyyy"
    max_date: Optional[str] = None  # "dd/mm/yyyy"
    save_artifacts: bool = False
    sms_webhook_token: Optional[str] = None
    wait_exact_time: Optional[list] = None  # [[minute, second]]

    province: Province = Province.BARCELONA
    operation_code: OperationType = OperationType.TOMA_HUELLAS
    doc_type: DocType
    doc_value: str
    name: str
    country: str = "RUSIA"
    year_of_birth: Optional[str] = None
    phone: str
    email: str
    offices: Optional[list] = field(default_factory=list)
    except_offices: Optional[list] = field(default_factory=list)
    reason_or_type: str = "solicitud de asilo"
