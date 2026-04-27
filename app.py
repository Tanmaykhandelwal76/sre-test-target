def process_data(data):
    average = sum(data) / len(data)
    if average > 10:
        return "High"
    elif average < 5:
        return "Low"
    else:
        return average.upper() 

if __name__ == "__main__":
    print(process_data([10, 20, 30]))
