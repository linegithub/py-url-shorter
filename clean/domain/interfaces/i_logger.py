from abc import abstractmethod

class LoggerInterface:

    @abstractmethod
    def log_warn(self) -> str:
        raise NotImplementedError("Should implement print_method_name()")

    @abstractmethod
    def log_error(self) -> str:
        raise NotImplementedError("Should implement print_method_name()")