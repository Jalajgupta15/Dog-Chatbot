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
                const imageUrl = `https://cdn2.thedogapi.com/images/${breed.reference_image_id}.jpg`;

                const breedInfoHTML = `
                    <div class="breed-info">
                        <img src="${imageUrl}" alt="${breed.name}">
                        <div>
                            <h2>${breed.name}</h2>
                            <p><strong>Temperament:</strong> ${breed.temperament}</p>
                            <p><strong>Life Span:</strong> ${breed.life_span}</p>
                            <p><strong>Bred For:</strong> ${breed.bred_for}</p>
                            <p><strong>Breed Group:</strong> ${breed.breed_group}</p>
                        </div>
                    </div>
                `;

                breedInfoDiv.innerHTML = breedInfoHTML;
            } else {
                breedInfoDiv.innerHTML = '<p>Breed not found. Please try again.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching breed info:', error);
            const breedInfoDiv = document.getElementById('breedInfo');
            breedInfoDiv.innerHTML = '<p>Error fetching breed info. Please try again later.</p>';
        });
}
