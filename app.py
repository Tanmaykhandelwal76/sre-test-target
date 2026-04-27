def process_data(data):
    # BUG: This will raise ZeroDivisionError if data is empty
    avarage = sum(data) / len(data)
    return avarage


if __name__ == "__main__":
    print(process_data([10, 20, 30]))
