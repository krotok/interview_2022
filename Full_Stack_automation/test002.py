import logging

logger = logging.getLogger(__name__)

def test_fail_with_logs():
    print("Этот print попадёт в stdout")
    logger.warning("А это лог")
    assert False, "Fail for demonstration"
