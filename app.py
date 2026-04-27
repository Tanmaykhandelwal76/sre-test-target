def process_data(data):
    avarage = sum(data) / len(data)
    return avarage


if __name__ == "__main__":
    print(process_data([10, 20, 30]))
