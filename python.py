import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_dog_breed_info(breed_name):
    api_url = f"https://api.thedogapi.com/v1/breeds/search?q={breed_name}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            breed_info = data[0]
            breed_name = breed_info['name']
            temperament = breed_info['temperament']
            lifespan = breed_info['life_span']
            image_url = f"https://cdn2.thedogapi.com/images/{breed_info['reference_image_id']}.jpg"
            bred_for = breed_info.get('bred_for', 'N/A')
            breed_group = breed_info.get('breed_group', 'N/A')

            # Example of food habits and likes/dislikes (dummy data)
            food_habits = "High-quality dog food, avoid grains"
            likes = "Playing fetch, being with family"
            dislikes = "Being left alone, loud noises"

            return {
                'breed_name': breed_name,
                'temperament': temperament,
                'lifespan': lifespan,
                'image_url': image_url,
                'bred_for': bred_for,
                'breed_group': breed_group,
                'food_habits': food_habits,
                'likes': likes,
                'dislikes': dislikes
            }
    return None

@app.route('/get_breed_info', methods=['GET'])
def get_breed_info():
    breed_name = request.args.get('breed_name')
    if breed_name:
        info = get_dog_breed_info(breed_name)
        if info:
            return jsonify(info)
    return jsonify({'error': 'Breed not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
