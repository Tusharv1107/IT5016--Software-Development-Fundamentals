def generate_brand_name():
    print("Welcome to the brand name generator")
    suberb = input("Which suberb did you grow up in? \n")
    state = input("What is the name of your state? \n")
    
    brand_name = f"{suberb.capitalize()} {state.capitalize()}"
    return brand_name

brand_name = generate_brand_name()
print("Your brand name is:", brand_name)
