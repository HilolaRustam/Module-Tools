#!/usr/bin/env node 

const fs = require("node:fs");
const path = require("node:path");

function parseArgs(args) {
  let showAll = false;
  let targetDir = ".";

  for (const arg of args) {
    if (arg === "-a") {
      showAll = true;
    } else if (!arg.startsWith("-")) {
      targetDir = arg;
    }
  }

  return { showAll, targetDir };
}

function listDirectory(dirPath, showAll) {
  let files = fs.readdirSync(dirPath);

  let hidden = [];
  let normal = files;

  if (!showAll) {
    normal = files.filter(file => !file.startsWith("."));
  } else {
    hidden = files.filter(file => file.startsWith("."));
    normal = files.filter(file => !file.startsWith("."));
    
  }

  normal.sort();
  hidden.sort();
  
  let result = [];

  if (showAll) {
    result.push(".","..");
  }
  result.push (...normal, ...hidden);

  return result; 
 
}

function main() {
  const args = process.argv.slice(2);
  const { showAll, targetDir } = parseArgs(args);

  const files = listDirectory(targetDir, showAll);
  console.log(files.join("\n"));
}

main();


