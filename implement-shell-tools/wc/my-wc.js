#!/usr/bin/env node

const fs = require("node:fs");

function countFile(filePath) {
  const content = fs.readFileSync(filePath, "utf8");

  const lines = content.split("\n").length - 1;
  const words = content.trim() ? content.trim().split(/\s+/).length : 0;
  const chars = Buffer.byteLength(content, "utf8");

  return { lines, words, chars };
}

function main() {
  const args = process.argv.slice(2);

  let flag = null;
  let files = [];

  for (const arg of args) {
    if (arg === "-l" || arg === "-w" || arg === "-c") {
      flag = arg;
    } else {
      files.push(arg);
    }
  }

  let totalLines = 0;
  let totalWords = 0;
  let totalChars = 0;

  for (const file of files) {
    const { lines, words, chars } = countFile(file);

    totalLines += lines;
    totalWords += words;
    totalChars += chars;

    if (flag === "-l") {
      console.log(`${lines} ${file}`);
    } else if (flag === "-w") {
      console.log(`${words} ${file}`);
    } else if (flag === "-c") {
      console.log(`${chars} ${file}`);
    } else {
      console.log(`${lines} ${words} ${chars} ${file}`);
    }
  }

  if (files.length > 1) {
    if (flag === "-l") {
      console.log(`${totalLines} total`);
    } else if (flag === "-w") {
      console.log(`${totalWords} total`);
    } else if (flag === "-c") {
      console.log(`${totalChars} total`);
    } else {
      console.log(`${totalLines} ${totalWords} ${totalChars} total`);
    }
  }
}

main();



