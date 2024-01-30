const fs = require('fs')
const axios = require('axios');

function cat(path){
    fs.readFile(path, 'utf8', function(err, data){
        if(err){
            console.error(`Error reading ${path}:\n ${err.message}`);
            process.exit(1);
        }
        else{
            console.log(data);
        }
    });
}

cat(process.argv[2]);

async function webcat(url){
    try{
        const response = await axios.get(url);
        console.log(response.data);
    }
    catch(err){
        console.error(`Error fetching ${url}:\n ${err.message}`); 
        process.exit(1);
    }
}

const arg = process.argv[2];
if (arg.startsWith('http')) {
    webcat(arg);
} else {
    cat(arg);
}