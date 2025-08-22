import os
import sys

from bcncita import (
    CustomerProfile,
    DocType,
    Office,
    OperationType,
    Province,
    try_cita,
)

from mako.template import Template


def build_customer_profile() -> CustomerProfile:
    """Construct and return a configured CustomerProfile."""
    return CustomerProfile(
        anticaptcha_api_key="... your key here ...",  # Set your Anti-Captcha API Key
        auto_captcha=False,  # If False, you must manually solve reCAPTCHA
        auto_office=True,
        chrome_driver_path="/usr/local/bin/chromedriver",
        save_artifacts=True,  # Save office info / screenshots
        province=Province.BARCELONA,
        operation_code=OperationType.RECOGIDA_DE_TARJETA,
        doc_type=DocType.NIE,
        doc_value="T1111111R",
        country="RUSIA",
        name="BORIS JOHNSON",
        phone="600000000",
        email="myemail@here.com",
        offices=[Office.BARCELONA_MALLORCA],
    )


def render_autofill_template(customer: CustomerProfile):
    """Render autofill.mako template with the given customer context."""
    template_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "bcncita",
        "template",
        "autofill.mako",
    )
    template = Template(filename=template_path)
    print(template.render(ctx=customer))


def main():
    customer = build_customer_profile()

    if "--autofill" in sys.argv:
        render_autofill_template(customer)
    else:
        try_cita(context=customer, cycles=200)


if __name__ == "__main__":
    main()
