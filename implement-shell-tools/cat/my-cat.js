#!/usr/bin/env node

const fs = require("fs");

const args = process.argv.slice(2);

let numberLines = false;
let numberNonEmpty = false;
let files = [];

//Parse arguments
for (const arg of args) {
  if (arg === "-n") {
    numberLines = true;
  } else if (arg === "-b") {
    numberNonEmpty = true;
  } else {
    files.push(arg);
  }
}
let count = 1;

//Process each files
files.forEach((file) => {
  const content = fs.readFileSync(file, "utf-8");
  const lines = content.split(/\r?\n/);
  if (lines[lines.length - 1] == ""){lines.pop();
  }

  lines.forEach((line) => {
    const shouldNumber = numberNonEmpty ? line !== "" : numberLines;
    
    if (numberNonEmpty && line === "") {
      process.stdout.write("\n");
    } else if (shouldNumber) {
      process.stdout.write(`${String(count).padStart(6)}  ${line}\n`);
      count++;
    } else {
      process.stdout.write(`${line}\n`);
    } 
    
  });
});
