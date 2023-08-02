document.addEventListener('DOMContentLoaded', () => {
    axios.get('/get_times_played')
        .then(response => {
            const timesPlayedElement = document.getElementById('times-played');
            timesPlayedElement.textContent = response.data.times_played;
        })
        .catch(error => {
            console.error('Error fetching times played:', error);
        });

    axios.get('/get_highest_score')
        .then(response => {
            const highestScoreElement = document.getElementById('highest-score');
            highestScoreElement.textContent = response.data.highest_score;
        })
        .catch(error => {
            console.error('Error fetching highest score:', error);
        });
});

const guessedWords = [];

function formSubmit(e){
    e.preventDefault();

    const guessInput = document.getElementById('word');
    const guess = guessInput.value.trim();

    if (guessedWords.includes(guess)) {
        // Word is a duplicate, handle accordingly (e.g., show a message)
        console.log('Duplicate word:', guess);
        return;
    }

    guessedWords.push(guess);

    axios.post('/check_guess', { word: guess })
            .then(response => {
                // Handle the response from the server
                const result = response.data.result;
                const messageElement = document.getElementById('message');
                const scoreElement = document.getElementById('score');

                if (result === 'ok') {
                    messageElement.textContent = 'Valid word! Great job!';
                    const wordLength = guess.length; // Calculate word length
                    const currentScore = parseInt(scoreElement.textContent); // Get current score
                    const newScore = currentScore + wordLength; // Calculate new score
                scoreElement.textContent = newScore; // Update score display

                axios.post('/update_score', { score: currentScore + guess.length })
                 .then(response => {
                     // Handle the response if needed
                })
                .catch(error => {
                console.error('Error updating score:', error);
                 });


                } else if (result === 'not-on-board') {
                    messageElement.textContent = 'The word is not on the board.';
                } else if (result === 'not-a-word') {
                    messageElement.textContent = 'The word is not valid.';
                } else {
                    messageElement.textContent = 'Something went wrong. Please try again.';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });


}


const form = document.getElementById('guess-form');
form.addEventListener('submit', formSubmit);    

let currentCount = 60;

function updateTimer(){
    const countDown = document.getElementById('count')
    countDown.textContent = currentCount;
}

function decrementTimer(){
    if(currentCount > 0){
        currentCount--;
        updateTimer();
    }
  

    if (currentCount === 0) {
        // Disable the form and timer when time is up
        const form = document.getElementById('guess-form');
        const guessInput = document.getElementById('word');
        const submitButton = document.querySelector('#guess-form button');

        guessInput.disabled = true;
        submitButton.disabled = true;
    }


}

updateTimer();

// Start the timer
const timerInterval = setInterval(decrementTimer, 1000);