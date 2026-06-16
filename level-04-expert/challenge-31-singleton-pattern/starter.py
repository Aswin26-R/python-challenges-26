class Singleton:
    """
    TODO:
    A base class that implements the Singleton pattern.
    Only ONE instance of this class (or any subclass) can exist.
    Every call to create an instance returns the SAME object.

    Implementation:
        Use a class variable _instance to store the single instance.
        Override __new__ to return the existing instance if it already exists.

        class Singleton:
            _instance = None

            def __new__(cls):
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                return cls._instance

    Test: s1 = Singleton(); s2 = Singleton(); assert s1 is s2
    """

    _instance = None

    def __new__(cls):
        # TODO: Return cls._instance if it exists, otherwise create it and store it
        pass


class AppConfig(Singleton):
    """
    TODO:
    A Singleton class for storing application configuration.
    All instances should share the same configuration dictionary.

    Methods:
        set(key, value) — stores key-value pair in config
        get(key, default=None) — retrieves value or returns default

    Example:
        config1 = AppConfig()
        config1.set("debug", True)
        config1.set("version", "1.0")

        config2 = AppConfig()
        config2.get("debug")    → True   (same object as config1)
        config2.get("version")  → "1.0"
        config2.get("missing")  → None

    IMPORTANT: Don't reset _config in __init__ if it already exists.
    Use this pattern to protect against re-initialization:
        def __init__(self):
            if not hasattr(self, '_initialized'):
                self._initialized = True
                self._config = {}
    """

    def __init__(self):
        # TODO: Initialize _config dict only once (protect against re-initialization)
        pass

    def set(self, key, value):
        """
        TODO: Store value under key in self._config
        """
        pass

    def get(self, key, default=None):
        """
        TODO: Return self._config.get(key, default)
        """
        pass


class Logger(Singleton):
    """
    TODO:
    A Singleton logger that accumulates log messages.
    All "instances" share the same list of messages.

    Methods:
        log(message) — adds message to the log
        get_logs()   — returns the list of all messages
        clear()      — empties the log

    Example:
        log1 = Logger()
        log1.log("App started")
        log1.log("Connected to DB")

        log2 = Logger()  ← same instance!
        log2.get_logs()  → ["App started", "Connected to DB"]
    """

    def __init__(self):
        # TODO: Initialize _messages list only once
        pass

    def log(self, message):
        """
        TODO: Append message to self._messages
        """
        pass

    def get_logs(self):
        """
        TODO: Return self._messages
        """
        pass

    def clear(self):
        """
        TODO: Clear all messages (self._messages = [])
        """
        pass
