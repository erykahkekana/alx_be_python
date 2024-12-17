#!/bin/bash
ask_weather = input("What's the weather like today? (sunny/rainy/cold):  ").lower()

if ask_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif ask_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif ask_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
