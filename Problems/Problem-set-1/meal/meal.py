def main():
    time_str = input("What time is it?")
    time =  convert(time_str)
    
    if 7 <= time < 8:
        print("Breakfast time")
    elif 12 <= time < 13:
        print("Lunch time")
    elif 18 <= time < 19:
        print("Dinner time")
    else:
        print("")
    


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    total_hours = hours + minutes/60
    
    return total_hours


if __name__ == "__main__":
    main()
