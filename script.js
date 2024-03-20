function getBreedInfo() {
    const breedName = document.getElementById('breedNameInput').value.trim().toLowerCase();
    const apiUrl = `https://api.thedogapi.com/v1/breeds/search?q=${breedName}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const breedInfoDiv = document.getElementById('breedInfo');
            breedInfoDiv.innerHTML = ''; // Clear previous content

            if (data.length > 0) {
                const breed = data[0];
                const breedName = breed.name;
                const temperament = breed.temperament;
                const lifespan = breed.life_span;

                breedInfoDiv.innerHTML = `
                    <h2>${breedName}</h2>
                    <p><strong>Temperament:</strong> ${temperament}</p>
                    <p><strong>Lifespan:</strong> ${lifespan}</p>
                    <!-- Add more information here as needed -->
                `;
            } else {
                breedInfoDiv.innerHTML = '<p>Breed not found.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching breed info:', error);
            const breedInfoDiv = document.getElementById('breedInfo');
            breedInfoDiv.innerHTML = '<p>Failed to retrieve breed information. Please try again later.</p>';
        });
}
