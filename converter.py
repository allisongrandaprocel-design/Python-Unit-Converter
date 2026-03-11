"""
UNIT CONVERTER - PYTHON
ENGINEER SOFTWARE - 1ST SEMESTER

Available categories:
  - Length       (meters, kilometers, miles, feet, inches)
  - Weight/Mass  (kilograms, grams, pounds, ounces)
  - Temperature  (Celsius, Fahrenheit, Kelvin)
  - Speed        (km/h, m/s, mph, knots)
  - Area         (m², km², hectares, acres)
  - Volume       (liters, milliliters, gallons, fluid ounces)
  - Time         (seconds, minutes, hours, days, weeks)
"""


# ──────────────────────────────────────────────
#  CONVERSION FUNCTIONS BY CATEGORY
# ──────────────────────────────────────────────

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Converts between length units using meters as the base unit."""
    to_meters = {
        "meter": 1,
        "kilometer": 1_000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1_609.344,
        "foot": 0.3048,
        "inch": 0.0254,
        "yard": 0.9144,
    }
    if from_unit not in to_meters or to_unit not in to_meters:
        raise ValueError(f"Unknown unit: '{from_unit}' or '{to_unit}'")
    return value * to_meters[from_unit] / to_meters[to_unit]


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """Converts between weight/mass units using kilograms as the base unit."""
    to_kg = {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000_001,
        "pound": 0.453_592,
        "ounce": 0.028_349_5,
        "ton": 1_000,
    }
    if from_unit not in to_kg or to_unit not in to_kg:
        raise ValueError(f"Unknown unit: '{from_unit}' or '{to_unit}'")
    return value * to_kg[from_unit] / to_kg[to_unit]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Converts between Celsius, Fahrenheit, and Kelvin."""
    # First convert to Celsius
    if from_unit == "celsius":
        in_celsius = value
    elif from_unit == "fahrenheit":
        in_celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        in_celsius = value - 273.15
    else:
        raise ValueError(f"Unknown unit: '{from_unit}'")

    # Then from Celsius to target
    if to_unit == "celsius":
        return in_celsius
    elif to_unit == "fahrenheit":
        return in_celsius * 9 / 5 + 32
    elif to_unit == "kelvin":
        return in_celsius + 273.15
    else:
        raise ValueError(f"Unknown unit: '{to_unit}'")


def convert_speed(value: float, from_unit: str, to_unit: str) -> float:
    """Converts between speed units using m/s as the base unit."""
    to_ms = {
        "meter_per_second": 1,
        "kilometer_per_hour": 1 / 3.6,
        "mile_per_hour": 0.44704,
        "knot": 0.514_444,
        "foot_per_second": 0.3048,
    }
    if from_unit not in to_ms or to_unit not in to_ms:
        raise ValueError(f"Unknown unit: '{from_unit}' or '{to_unit}'")
    return value * to_ms[from_unit] / to_ms[to_unit]


def convert_area(value: float, from_unit: str, to_unit: str) -> float:
    """Converts between area units using m² as the base unit."""
    to_m2 = {
        "square_meter": 1,
        "square_kilometer": 1_000_000,
        "square_centimeter": 0.0001,
        "hectare": 10_000,
        "acre": 4_046.86,
        "square_foot": 0.092_903,
        "square_mile": 2_589_988.11,
    }
    if from_unit not in to_m2 or to_unit not in to_m2:
        raise ValueError(f"Unknown unit: '{from_unit}' or '{to_unit}'")
    return value * to_m2[from_unit] / to_m2[to_unit]


def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """Converts between volume units using liters as the base unit."""
    to_liters = {
        "liter": 1,
        "milliliter": 0.001,
        "cubic_meter": 1_000,
        "cubic_centimeter": 0.001,
        "us_gallon": 3.785_41,
        "uk_gallon": 4.546_09,
        "fluid_ounce": 0.029_573_5,
        "cup": 0.236_588,
        "tablespoon": 0.014_787,
        "teaspoon": 0.004_929,
    }
    if from_unit not in to_liters or to_unit not in to_liters:
        raise ValueError(f"Unknown unit: '{from_unit}' or '{to_unit}'")
    return value * to_liters[from_unit] / to_liters[to_unit]


def convert_time(value: float, from_unit: str, to_unit: str) -> float:
    """Converts between time units using seconds as the base unit."""
    to_seconds = {
        "second": 1,
        "minute": 60,
        "hour": 3_600,
        "day": 86_400,
        "week": 604_800,
        "month": 2_629_800,       # average month (365.25/12 days)
        "year": 31_557_600,       # Julian year
        "millisecond": 0.001,
        "microsecond": 0.000_001,
    }
    if from_unit not in to_seconds or to_unit not in to_seconds:
        raise ValueError(f"Unknown unit: '{from_unit}' or '{to_unit}'")
    return value * to_seconds[from_unit] / to_seconds[to_unit]


# ──────────────────────────────────────────────
#  MENU DATA (display name + units)
# ──────────────────────────────────────────────

CATEGORIES = {
    "1": {
        "name": "📏 Length",
        "function": convert_length,
        "units": ["meter", "kilometer", "centimeter", "millimeter",
                  "mile", "foot", "inch", "yard"],
    },
    "2": {
        "name": "⚖️  Weight / Mass",
        "function": convert_weight,
        "units": ["kilogram", "gram", "milligram", "pound", "ounce", "ton"],
    },
    "3": {
        "name": "🌡️  Temperature",
        "function": convert_temperature,
        "units": ["celsius", "fahrenheit", "kelvin"],
    },
    "4": {
        "name": "💨 Speed",
        "function": convert_speed,
        "units": ["meter_per_second", "kilometer_per_hour",
                  "mile_per_hour", "knot", "foot_per_second"],
    },
    "5": {
        "name": "🟦 Area",
        "function": convert_area,
        "units": ["square_meter", "square_kilometer", "square_centimeter",
                  "hectare", "acre", "square_foot", "square_mile"],
    },
    "6": {
        "name": "🧪 Volume",
        "function": convert_volume,
        "units": ["liter", "milliliter", "cubic_meter", "cubic_centimeter",
                  "us_gallon", "uk_gallon", "fluid_ounce", "cup",
                  "tablespoon", "teaspoon"],
    },
    "7": {
        "name": "⏱️  Time",
        "function": convert_time,
        "units": ["second", "minute", "hour", "day", "week",
                  "month", "year", "millisecond", "microsecond"],
    },
}


# ──────────────────────────────────────────────
#  INTERFACE HELPERS
# ──────────────────────────────────────────────

def divider(char: str = "─", width: int = 54) -> None:
    print(char * width)


def show_main_menu() -> None:
    divider("═")
    print("         🔄  UNIT CONVERTER  🔄")
    divider("═")
    for key, data in CATEGORIES.items():
        print(f"  [{key}]  {data['name']}")
    print("  [0]  🚪 Exit")
    divider()


def show_units(units: list[str]) -> None:
    divider()
    print("  Available units:")
    for i, u in enumerate(units, start=1):
        print(f"    {i:>2}. {u}")
    divider()


def choose_unit(prompt: str, units: list[str]) -> str:
    """Asks the user to choose a unit by number."""
    while True:
        entry = input(prompt).strip()
        if entry.isdigit():
            idx = int(entry) - 1
            if 0 <= idx < len(units):
                return units[idx]
        print(f"  ⚠️  Please choose a number between 1 and {len(units)}.")


def ask_value(prompt: str) -> float:
    """Prompts the user for a floating-point number."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("  ⚠️  Please enter a valid number (e.g. 3.14).")


def format_result(value: float) -> str:
    """Formats the result: integer if possible, otherwise with decimals."""
    if value == int(value) and abs(value) < 1e12:
        return f"{int(value):,}"
    return f"{value:,.6f}".rstrip("0").rstrip(".")


# ──────────────────────────────────────────────
#  MAIN FLOW
# ──────────────────────────────────────────────

def perform_conversion(category: dict) -> None:
    """Guides the user through a complete conversion."""
    units    = category["units"]
    function = category["function"]

    show_units(units)

    from_unit = choose_unit("  FROM unit (number): ", units)
    to_unit   = choose_unit("  TO   unit (number): ", units)

    if from_unit == to_unit:
        print("\n  ℹ️  Origin and destination are the same. Value unchanged.\n")
        return

    value = ask_value(f"\n  Value in [{from_unit}]: ")

    try:
        result = function(value, from_unit, to_unit)
        divider()
        print(f"\n  ✅  {format_result(value)} {from_unit}")
        print(f"      =  {format_result(result)} {to_unit}\n")
        divider()
    except ValueError as e:
        print(f"\n  ❌  Error: {e}\n")


def main() -> None:
    """Main program loop."""
    print("\n  Welcome to the Unit Converter 🎉")
    print("  Built with Python — GitHub Project\n")

    while True:
        show_main_menu()
        option = input("  Choose a category: ").strip()

        if option == "0":
            print("\n  Goodbye! 👋\n")
            break
        elif option in CATEGORIES:
            print(f"\n  → {CATEGORIES[option]['name']}\n")
            perform_conversion(CATEGORIES[option])

            again = input("  Perform another conversion? (y/n): ").strip().lower()
            if again != "y":
                print("\n  Goodbye! 👋\n")
                break
        else:
            print("  ⚠️  Invalid option. Please try again.\n")


# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
