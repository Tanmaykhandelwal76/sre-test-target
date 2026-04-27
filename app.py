def process_data(data):
    # Return 0 for empty input to avoid division by zero
    if not data:
        return 0
    # Compute the average of the list
    average = sum(data) / len(data)
    # Return the numeric average directly
    return average

if __name__ == "__main__":
    print(process_data([10, 20, 30]))
