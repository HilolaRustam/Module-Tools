#!/usr/bin/env node

const fs = require("node:fs");
const path = require("node:path");

function main() {
  const args = process.argv.slice(2);

  const {
    showAll,
    onePerLine,
    targetDir,
    unknownFlags
  } = parseArgs(args);

  if (unknownFlags.length > 0) {
    console.error(
      `warning: unknown option(s): ${unknownFlags.join(", ")}`
    );
  }

  let files = readDirectory(targetDir);

  files = applyFilters(files, showAll);
  files = sortFiles(files);

  const output = render(files, onePerLine);

  console.log(output);
}

main();

function parseArgs(args) {
  let showAll = false;
  let onePerLine = false;
  let targetDir = ".";
  const unknownFlags = [];

  const knownFlags = new Set(["-a", "-1"]);

  for (const arg of args) {
    if (knownFlags.has(arg)) {
      if (arg === "-a") showAll = true;
      if (arg === "-1") onePerLine = true;
    } else if (arg.startsWith("-")) {
      unknownFlags.push(arg);
    } else {
      targetDir = arg;
    }
  }

  return { showAll, onePerLine, targetDir, unknownFlags };
}

function readDirectory(dir) {
  return fs.readdirSync(dir);
}

function applyFilters(files, showAll) { 
  if (!showAll) {
    return files.filter(f => !f.startsWith("."));
  }

    return [".", "..", ...files];
  }
function sortFiles(files) {
  return files.sort();
}

function render(files, onePerLine) {
  if (onePerLine) {
    return files.join("\n");
  }

  // default format (simple column simulation)
  return files.join("  ");
}



