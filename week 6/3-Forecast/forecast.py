def forecast(days) :

    snowing = days.count("snow")
    raining = days.count("rain")
    suns = days.count("sunshine")

    if raining > snowing and raining > suns :
        return "rain"

    elif suns > raining and suns > snowing :
        return "sunshine"

    elif snowing > suns and snowing > raining:
        return "snow"

    elif suns == snowing and suns!= raining:
        return "rain"

    elif suns == raining and raining != snowing:
        return "snow"

    elif raining == snowing and raining != suns:
        return "suns"

    elif suns == snowing and snowing == raining and suns == raining:
        return days[len(days)-1]

print(forecast(["snow", "snow", "rain", "sunshine"]))
print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
print(forecast(["rain", "rain", "sunshine", "sunshine"]))