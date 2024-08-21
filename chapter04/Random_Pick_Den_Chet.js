

let minhCOunt = 0;
let datCount = 0;

let randomChoice = () => {
    return Math.floor(Math.random() * 2);
}

for (let i = 0; i < 100; i++) {
    if (randomChoice() == 0)
        minhCOunt++;
    else
        datCount++;
}


console.log(minhCOunt / datCount);


