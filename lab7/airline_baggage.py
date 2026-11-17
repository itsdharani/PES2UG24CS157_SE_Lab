import math


def parse_booking(code):
    if not isinstance(code, str):
        return None

    parts = code.strip().split('-')

    if len(parts) != 3:
        return None

    airline, flight, seat = parts

    if not airline.isalpha():
        return None

    if not flight.isdigit():
        return None

    if len(seat) < 2:
        return None

    seat_number = seat[:-1]
    seat_letter = seat[-1]

    if not seat_number.isdigit() or not seat_letter.isalpha():
        return None

    return airline.upper(), int(flight), seat_letter.upper()


def total_weight(weights_csv):
    if not isinstance(weights_csv, str):
        return None

    try:
        parts = weights_csv.split(',')

        if not parts or any(not w.strip() for w in parts):
            return None

        weights = [float(w.strip()) for w in parts]

        if any(not math.isfinite(w) or w < 0 for w in weights):
            return None

        return sum(weights)

    except (ValueError, OverflowError):
        return None


def tag_label(name):
    if not isinstance(name, str):
        return None

    parts = name.split()

    if len(parts) < 2:
        return None

    return parts[0][0].upper() + '. ' + parts[-1].upper()


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter a booking code (e.g. AI-203-12A): ")
    result = parse_booking(user_input)
    print("Airline, Flight and Seat Letter:", result)

    print("\n==== Running total_weight ====")
    user_input = input("Enter bag weights in kg as CSV (e.g. 12.5,7,23): ")
    result = total_weight(user_input)
    print("Total Weight:", result)

    print("\n==== Running tag_label ====")
    user_input = input("Enter a passenger name (first and last): ")
    result = tag_label(user_input)
    print("Tag Label:", result)


if __name__ == "__main__":
    main()
