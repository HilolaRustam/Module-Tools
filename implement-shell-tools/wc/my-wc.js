#!/usr/bin/env node

const fs = require("node:fs");

function countFile(filePath) {
  const stats = fs.statSync(filePath);

  if (!stats.isFile()) {
    console.warn(`${filePath} is not a file, skipping`);
    return null;
  }
  const content = fs.readFileSync(filePath, "utf8");

  const lines = content.split("\n").length - 1;
  const words = content.trim() ? content.trim().split(/\s+/).length : 0;
  const chars = Buffer.byteLength(content, "utf8");

  return { lines, words, chars };
}

function main() {
  const args = process.argv.slice(2);

  let flags = [];
  let files = [];

  // 1 Parse args
  for (const arg of args) {
    if (arg === "-l" || arg === "-w" || arg === "-c") {
      flags.push(arg);
    } else {
      files.push(arg);
    }
  }

  //2 Helper function that decides what to print

  function formatOutput(counts, files) {
    const parts = [];

    // if no flags show everything
    const showAll = flags.length === 0;

    if (showAll || flags.includes("-l"))parts.push(counts.lines);
    if (showAll || flags.includes("-w"))parts.push(counts.words);
    if (showAll || flags.includes("-c"))parts.push(counts.chars);

    parts.push(files);

    return parts.join(" ");
  }
  // 3 totals
  let totalLines = 0;
  let totalWords = 0;
  let totalChars = 0;


  // 4 per-file output
  for (const file of files) {
    const counts = countFile(file);
    if (!counts) continue;

    totalLines += counts.lines;
    totalWords += counts.words;
    totalChars += counts.chars;

    console.log(formatOutput(counts, files));
  }
  // 5 Total output (only if multiple files)
  if (files.length > 1) {
    const totalCounts = {
      lines: totalLines,
      words: totalWords,
      chars: totalChars,
    };
    console.log(formatOutput(totalCounts,"total"));
  }
}

main();



