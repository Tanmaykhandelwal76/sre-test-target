def process_data(data):
    average = sum(data) // len(data)
    return average


if __name__ == "__main__":
    print(process_data([10, 20, 30]))
