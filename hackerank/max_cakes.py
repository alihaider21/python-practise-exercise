def birthdayCakeCandles(candles):
    # Write your code here
    m = max(candles)
    return candles.count(m)

cand = [18, 90, 90, 13, 90, 75, 90, 8, 90, 43]
print(birthdayCakeCandles(cand))