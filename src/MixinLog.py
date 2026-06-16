class MixinLog:
    def __init__(self) -> None:
        super().__init__()
        print(repr(self))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}, "  # type: ignore[attr-defined]
            f"description={self.description!r}, "  # type: ignore[attr-defined]
            f"price={self.price}, "  # type: ignore[attr-defined]
            f"quantity={self.quantity})"  # type: ignore[attr-defined]
        )  # type: ignore[attr-defined]
