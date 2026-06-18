class MixinLog:
    def __init__(self) -> None:
        super().__init__()
        print(repr(self))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"({self.name!r}, "  # type: ignore[attr-defined]
            f"{self.description!r}, "  # type: ignore[attr-defined]
            f"{self.price}, "  # type: ignore[attr-defined]
            f"{self.quantity})"  # type: ignore[attr-defined]
        )  # type: ignore[attr-defined]
