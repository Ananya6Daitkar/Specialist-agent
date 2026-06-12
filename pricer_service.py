import modal

app = modal.App("pricer-service")


@app.cls()
class Pricer:
    @modal.method()
    def price(self, description: str) -> float:
        description = description.lower()

        if "iphone" in description:
            return 120000.0
        elif "macbook" in description:
            return 150000.0
        elif "samsung" in description:
            return 80000.0
        else:
            return 50000.0