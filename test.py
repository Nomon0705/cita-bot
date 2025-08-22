import logging
import os
import unittest

from bcncita import (
    CustomerProfile,
    DocType,
    Office,
    OperationType,
    Province,
    init_wedriver,
    start_with,
    try_cita,
)


class TestBot(unittest.TestCase):
    def setUp(self):
        """Common test parameters for all tests."""
        self.params = {
            "chrome_driver_path": "chromedriver",
            "auto_office": True,
            "auto_captcha": True,
            "name": "BORIS JOHNSON",
            "doc_type": DocType.PASSPORT,
            "doc_value": "132435465",
            "phone": "600000000",
            "email": "ghtvgdr@affecting.org",
        }

    def test_cita_initial_flow(self):
        """Test cita flow with BREXIT operation in Barcelona."""
        customer = CustomerProfile(
            **self.params,
            province=Province.BARCELONA,
            operation_code=OperationType.BREXIT,
            offices=[Office.BARCELONA],
        )

        with self.assertLogs(level=logging.INFO) as logs:
            try_cita(context=customer, cycles=1)

        expected_logs = [
            "INFO:root:\x1b[33m[Attempt 1/1]\x1b[0m",
            "INFO:root:[Step 1/6] Personal info",
            "INFO:root:[Step 2/6] Office selection",
            "INFO:root:[Step 3/6] Contact info",
            "INFO:root:[Step 4/6] Cita attempt -> selection hit!",
        ]
        for log in expected_logs:
            self.assertIn(log, logs.output)

    def test_instructions_page_for_all_provinces(self):
        """Ensure instructions page loads for all provinces."""
        driver = init_wedriver(CustomerProfile(**self.params))

        for province in Province:
            customer = CustomerProfile(
                **self.params,
                pro
