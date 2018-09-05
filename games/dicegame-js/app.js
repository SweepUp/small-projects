/*
GAME RULES:
- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game
*/

var scores, activePlayer, roundScore, playing, oldDice, winScore;
init();

document.querySelector('.btn-roll').addEventListener('click', function() {
	if (playing) {
		var newDice = Math.floor(Math.random() * 6) + 1;

		var diceDOM = document.querySelector(".dice");
		diceDOM.style.display = 'block';
		diceDOM.src = 'dice-' + newDice + '.png';

		if (newDice === 6 && oldDice === 6) {
			scores[activePlayer] = 0;
        	document.getElementById('score-' + activePlayer).textContent = 0;
        	nextPlayer();
		}

		else if (newDice !== 1) {
			oldDice = newDice;
			roundScore += newDice;
			document.getElementById("current-" + activePlayer).textContent = roundScore;
		}

		else {
			nextPlayer();
		}
	}
})

function nextPlayer() {
    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
    roundScore = 0;
    oldDice = 0;

    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';

    document.querySelector('.player-0-panel').classList.toggle('active');	//.classList.remove('active');
    document.querySelector('.player-1-panel').classList.toggle('active');	//.classList.add('active');

    document.querySelector('.dice').style.display = 'none';
}

document.querySelector('.btn-hold').addEventListener('click', function() {
	if (playing) {

		winScore = document.querySelector('.final-score').value;
		winScore ? winScore = document.querySelector('.final-score').value : winScore = 100;

        scores[activePlayer] += roundScore;
        document.getElementById('score-' + activePlayer).textContent = scores[activePlayer];

        if (scores[activePlayer] >= winScore) {
            document.getElementById('name-' + activePlayer).textContent = 'Winner!';
            document.querySelector('.dice').style.display = 'none';
            document.querySelector('.player-' + activePlayer + '-panel').classList.add('winner');
            document.querySelector('.player-' + activePlayer + '-panel').classList.remove('active');
            playing = false;
        } 
        else {
            nextPlayer();
        }
	}
})

document.querySelector('.btn-new').addEventListener('click', init);

function init() {
	scores = [0, 0];
	activePlayer = 0;
	roundScore = 0;
	playing = true;
	document.querySelector(".dice").style.display = 'none';
	document.getElementById("score-0").textContent = '0';
	document.getElementById("score-1").textContent = '0';
	document.getElementById("current-0").textContent = '0';
	document.getElementById("current-1").textContent = '0';
	document.getElementById('name-0').textContent = 'Player 1';
    document.getElementById('name-1').textContent = 'Player 2';
    document.querySelector('.player-0-panel').classList.remove('winner');
    document.querySelector('.player-1-panel').classList.remove('winner');
    document.querySelector('.player-0-panel').classList.remove('active');
    document.querySelector('.player-1-panel').classList.remove('active');
    document.querySelector('.player-0-panel').classList.add('active');
}