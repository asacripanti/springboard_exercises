let url = "http://numbersapi.com";
let favNum = 7;

//1.
async function ptOne(){
    let data = await $.getJSON(`${url}/${favNum}?json`);
    console.log(data);
}
ptOne();

//2.

const multNums = [5, 44, 18];
async function part2(){
    let data = await $.getJSON(`${url}/${multNums}?json`);
    console.log(data);
}

part2();

//3.
async function ptThree(){
    let facts = await Promise.all(
        Array.from({ length: 4 }, () => $.getJSON(`${url}/${favNum}?json`))
    );
    facts.forEach(data => {
        $('body').append(`<p>${data.text}</p>`);
    })
}
ptThree();