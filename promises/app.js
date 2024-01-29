let url = "http://numbersapi.com"
let number = 7;

// 1.
$.getJSON(`${url}/${number}?json`).then(data => {
    console.log(data);
});

// 2.

let multNums = [4, 5, 8];
$.getJSON(`${url}/${multNums}?json`).then(data => {
    console.log(data);
});

// 3.
Promise.all(
    Array.from({ length: 4 }, () => {
      return $.getJSON(`${url}/${number}?json`);
    })
  ).then(facts => {
    facts.forEach(data => $("body").append(`<p>${data.text}</p>`));
  });

  //Part 2
$(function(){
  let secondUrl = 'https://deckofcardsapi.com/api/deck';

    // 1.
    $.getJSON(`${secondUrl}/new/draw/`).then(data => {
      let { suit, value } = data.cards[0];
      console.log(`${value.toLowerCase()} of ${suit.toLowerCase()}`);
    });

      // 2.
  let firstCard = null;
  $.getJSON(`${secondUrl}/new/draw/`)
    .then(data => {
      firstCard = data.cards[0];
      let deckId = data.deck_id;
      return $.getJSON(`${secondUrl}/${deckId}/draw/`);
    })
    .then(data => {
      let secondCard = data.cards[0];
      [firstCard, secondCard].forEach(function(card) {
        console.log(
          `${card.value.toLowerCase()} of ${card.suit.toLowerCase()}`
        );
      });
    });

    // 3.
  let deckId = null;
  let $btn = $('button');
  let $cardArea = $('#card-area');

  $.getJSON(`${secondUrl}/new/shuffle/`).then(data => {
    deckId = data.deck_id;
    $btn.show();
  });

  $btn.on('click', function() {
    $.getJSON(`${secondUrl}/${deckId}/draw/`).then(data => {
      let cardSrc = data.cards[0].image;
      let angle = Math.random() * 90 - 45;
      let randomX = Math.random() * 40 - 20;
      let randomY = Math.random() * 40 - 20;
      $cardArea.append(
        $('<img>', {
          src: cardSrc,
          css: {
            transform: `translate(${randomX}px, ${randomY}px) rotate(${angle}deg)`
          }
        })
      );
      if (data.remaining === 0) $btn.remove();
    });
  });
})



  

  
