def process_data(data):
    if not data:
        return 0
    average = sum(data) // len(data)
    return average


if __name__ == "__main__":
    print(process_data([10, 20, 30]))
