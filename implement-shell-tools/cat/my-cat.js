#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

let numberLines = false;
let numberNonEmpty = false;

if (args[0] === "-n") {
  numberLines = true;
  args.shift();
} else if (args[0] === "-b") {
  numberNonEmpty = true;
  args.shift();
}
let count = 1;

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
