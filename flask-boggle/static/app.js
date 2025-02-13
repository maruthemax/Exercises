let score = 0;
let guessedWords = new Set();
let time = 60;

// Timer Logic
const timer = setInterval(() => {
    time--;
    $("#timer").text(time);
    if (time === 0) {
        clearInterval(timer);
        $("#guess-form").hide();
        alert("Time's up!");
        postScore();
    }
}, 1000);

// Handle Word Submission
$("#guess-form").on("submit", async function (evt) {
    evt.preventDefault();
    const word = $("#guess-input").val().toUpperCase();
    if (guessedWords.has(word)) {
        $("#result").text("Word already guessed!");
        return;
    }
    const response = await axios.post("/check-word", { word });
    const result = response.data.result;
    if (result === "ok") {
        guessedWords.add(word);
        score += word.length;
        $("#score").text(score);
        $("#result").text("Good word!");
    } else if (result === "not-a-word") {
        $("#result").text("Not a valid word!");
    } else if (result === "not-on-board") {
        $("#result").text("Word not on board!");
    }
    $("#guess-input").val("");
});

// Post Score to Backend
async function postScore() {
    const response = await axios.post("/post-score", { score });
    const { high_score, games_played } = response.data;
    alert(`Game over! High score: ${high_score}. Games played: ${games_played}.`);
}
