def process_data(data):
    if not data:
        return 0
    return sum(data) / len(data)


if __name__ == "__main__":
    print(process_data([10, 20, 30]))
