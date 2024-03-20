import requests

def get_dog_breed_info(breed_name):
    # Get data from Dog CEO's Dog API
    api_url = f"https://api.thedogapi.com/v1/breeds/search?q={breed_name}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            breed_info = data[0]
            breed_name = breed_info['name']
            temperament = breed_info['temperament']
            lifespan = breed_info['life_span']
            image_url = breed_info['image']['url'] if 'image' in breed_info else None
            # Additional hardcoded data (can be extended with more attributes)
            favorite_food = "Varies by individual, but high-quality dog food is recommended."
            color = "Varies depending on the breed."
            best_hobby = "Activities that match the breed's characteristics, such as fetching, herding, etc."
            likes = "Depends on the individual dog, but many enjoy playtime, walks, and spending time with their owners."
            dislikes = "Can vary widely, but some dogs may dislike certain noises, strangers, or other animals."
            attractions = "Dog parks, training classes, and activities that stimulate their minds and bodies."
            
            # Print the information
            print(f"Breed: {breed_name}")
            print(f"Temperament: {temperament}")
            print(f"Lifespan: {lifespan}")
            print(f"Favorite Food: {favorite_food}")
            print(f"Color: {color}")
            print(f"Best Hobby: {best_hobby}")
            print(f"Likes: {likes}")
            print(f"Dislikes: {dislikes}")
            print(f"Attractons: {attractions}")
            if image_url:
                print(f"Image: {image_url}")
        else:
            print("Breed not found.")
    else:
        print("Failed to retrieve data from the API.")

if __name__ == "__main__":
    breed_name = input("Enter the name of the dog breed: ").strip().lower()
    get_dog_breed_info(breed_name)
