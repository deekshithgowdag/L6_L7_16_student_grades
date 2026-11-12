def average_marks(marks_csv):
    try:
        if not isinstance(marks_csv, str) or not marks_csv.strip():
            return None

        marks = [int(m.strip()) for m in marks_csv.split(',')]

        return round(sum(marks) / len(marks), 2)

    except (ValueError, TypeError, ZeroDivisionError):
        return None


def parse_srn(srn):
    try:
        if not isinstance(srn, str):
            return None

        if len(srn) != 13:
            return None

        if (not srn[:4].isalnum()
                or not srn[4:6].isalpha()
                or not srn[6:8].isdigit()
                or not srn[8:10].isalpha()
                or not srn[10:13].isdigit()):
            return None

        return srn[:4], int(srn[6:8]), srn[8:10]

    except (ValueError, TypeError):
        return None


def short_name(full_name):
    try:
        if not isinstance(full_name, str):
            return None

        parts = full_name.split()

        if len(parts) < 2:
            return None

        first = parts[0]
        last = parts[-1]

        return first[0].upper() + ". " + last.capitalize()

    except (ValueError, TypeError, IndexError):
        return None


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    print("Short Name:", result)


if __name__ == "__main__":
    main()