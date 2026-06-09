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

//Process each files
args.forEach((file) => {
  const content = fs.readFileSync(file, "utf-8");
  const lines = content.split(/\r?\n/);

  let count = 1;

  lines.forEach((line) => {
    const shouldNumber = numberLines || (numberNonEmpty && line !== "");

    if (shouldNumber) {
      console.log(`${count} ${line}`);
      count++;
    } else {
      console.log(line);
    }
  });
});
