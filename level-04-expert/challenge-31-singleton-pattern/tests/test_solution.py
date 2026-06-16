import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import Singleton, AppConfig, Logger


@pytest.fixture(autouse=True)
def reset_singletons():
    Singleton._instance = None
    AppConfig._instance = None
    Logger._instance = None
    yield
    Singleton._instance = None
    AppConfig._instance = None
    Logger._instance = None


class TestSingleton:
    def test_same_instance(self):
        s1 = Singleton()
        s2 = Singleton()
        assert s1 is s2, "Singleton() should always return the same instance"

    def test_three_calls_same_instance(self):
        s1 = Singleton()
        s2 = Singleton()
        s3 = Singleton()
        assert s1 is s2 is s3


class TestAppConfig:
    def test_same_instance(self):
        c1 = AppConfig()
        c2 = AppConfig()
        assert c1 is c2

    def test_set_and_get(self):
        config = AppConfig()
        config.set("debug", True)
        assert config.get("debug") is True

    def test_shared_state(self):
        config1 = AppConfig()
        config1.set("version", "1.0")

        config2 = AppConfig()
        assert config2.get("version") == "1.0"

    def test_get_default(self):
        config = AppConfig()
        assert config.get("missing_key") is None

    def test_get_custom_default(self):
        config = AppConfig()
        assert config.get("missing", "fallback") == "fallback"

    def test_update_value(self):
        config = AppConfig()
        config.set("key", "old")
        config.set("key", "new")
        assert config.get("key") == "new"


class TestLogger:
    def test_same_instance(self):
        l1 = Logger()
        l2 = Logger()
        assert l1 is l2

    def test_log_message(self):
        logger = Logger()
        logger.log("Test message")
        assert "Test message" in logger.get_logs()

    def test_shared_messages(self):
        log1 = Logger()
        log1.log("First message")

        log2 = Logger()
        log2.log("Second message")

        assert "First message" in log1.get_logs()
        assert "Second message" in log1.get_logs()

    def test_get_logs_returns_list(self):
        logger = Logger()
        assert isinstance(logger.get_logs(), list)

    def test_clear(self):
        logger = Logger()
        logger.log("message")
        logger.clear()
        assert logger.get_logs() == []
