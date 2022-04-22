class Parser:
    """
    Parser parent class
    :param name: Name of parsed service
    :type name: str
    """

    def __init__(self, name) -> None:
        """
        Constructor method
        :param name:
        """
        super().__init__()

    def parse(self, sub):
        """
        Parse service
        :param sub: flag for subscription
        :type sub: bool
        """
        pass

    def save(self):
        """
        Save parsed information to the db
        """
        pass


class KpParser(Parser):
    """
    Parser class for KinoPoisk. It is essentially an extended class of the Parser
    """

    def parse(self, sub):
        """Overrides method of Parser"""
        pass
    pass


class OkkoParser(Parser):
    """
    Parser class for Okko. It is essentially an extended class of the Parser
    """

    def parse(self, sub):
        """Overrides method of Parser"""
        pass
    pass
