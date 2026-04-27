def process_data(data):
    # Return 0 for empty input to avoid ZeroDivisionError
    if not data:
        return 0
    avarage = sum(data) // len(data)
    return avarage


if __name__ == "__main__":
    print(process_data([10, 20, 30]))
