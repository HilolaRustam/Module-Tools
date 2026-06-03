#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

let numberLines = false;
let numberNonEmpty = false;
let files = [];

for (const arg of args) {
if (arg === "-n") {
  numberLines = true;
} else if (arg === "-b") {
  numberNonEmpty = true;
} else {
  files.push(arg);
}   
};

args.forEach((file) => {
  const content = fs.readFileSync(file, "utf-8");
  const lines = content.split(/\r?\n/);
  

  if (numberLines){ 
    lines.forEach((line) => {
      console.log(`${count} ${line}`);
      count++;
    });
  } else if (numberNonEmpty){
    lines.forEach((line) => {
    if (line !== "") {
      console.log(`${count} ${line}`);
      count++;
    } else {
      console.log("");
    }
  });
} else {
console.log(content);
  }
});
