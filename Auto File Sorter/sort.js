const fs = require('fs');
const { exec } = require('child_process');

const sortDir = "Sort";
const filesToSort = fs.readdirSync(sortDir);
const files = [];

// Initialize counters
let successCount = 0;
let failCount = 0;

// Get all files and folders in the current directory
fs.readdirSync('.').forEach(j => {
    if (j[0] === "A") {
        files.push(j);
    } else if (j === "Sort" || j === "File Sorter.exe" || j === "sort.py" || j === "sort.js" || j === "sort.exe") {
        // Skip these files/folders
    } else {
        exec(`msg * "Folder ${j} not named right. Family code has to start with A! (E.g. A001${j.slice(4)})"`);
    }
});

// Move files to their respective folders
filesToSort.forEach(fileToSort => {
    let moved = false; // Flag to track if the file was moved successfully
    files.forEach(folder => {
        if (folder.slice(0, 4) === fileToSort.slice(0, 4)) {
            try {
                fs.renameSync(`${sortDir}/${fileToSort}`, `${folder}/${fileToSort}`);
                successCount++; // Increment success counter
                moved = true; // Mark as moved
            } catch (err) {
                console.error(`Error moving file ${fileToSort}: ${err.message}`);
                failCount++; // Increment fail counter
            }
        }
    });
});

// Check for files in the Sort directory that couldn't be moved
fs.readdirSync(sortDir).forEach(file => {
    exec(`msg * "No Folder with the family code ${file.slice(0, 4)}"`);
    failCount++; // Increment fail counter for files that couldn't be moved
});

// Display the results
console.log(`Files sorted successfully: ${successCount}`);
console.log(`Files that failed: ${failCount}`);
exec(`msg * "Success: ${successCount} Fail: ${failCount}"`);