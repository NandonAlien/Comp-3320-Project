const memorySize = 256; // 256 bytes of memory
const pageSize = 16; // 16 bytes per page
const numPages = memorySize / pageSize; // 16 pages in total

const memory = new Uint8Array(memorySize); // the actual memory

let programLoaded = false; // flag to indicate if a program is currently loaded
let pagesUsed = new Set(); // set of page numbers currently in use

// get the page number for a given address
function getPage(address) {
  return Math.floor(address / pageSize);
}

// load a program into memory
function loadProgram(program) {
  // make sure no program is currently loaded
  if (programLoaded) {
    alert("A program is already loaded!");
    return;
  }

  // calculate the number of pages required for the program
  const numProgramPages = Math.ceil(program.length / pageSize);

  // check if there are enough free pages in memory
  if (numProgramPages > numPages - pagesUsed.size) {
    alert("Not enough free memory!");
    return;
  }

  // load the program into memory
  for (let i = 0; i < program.length; i++) {
    const address = i;
    const value = program[i];
    memory[address] = value;
    pagesUsed.add(getPage(address));
  }

  // update the usage bar
  updateUsage();

  programLoaded = true;
}

// unload the currently loaded program from memory
function unloadProgram() {
  // make sure a program is currently loaded
  if (!programLoaded) {
    alert("No program loaded!");
    return;
  }

  // clear the memory used by the program
  for (let i = 0; i < memory.length; i++) {
    if (pagesUsed.has(getPage(i))) {
      memory[i] = 0;
    }
  }
  pagesUsed.clear();

  // update the usage bar
  updateUsage();

  programLoaded = false;
}

// update the usage bar
function updateUsage() {
  const usageBar = document.getElementById("usage-bar-fill");
  const usageText = document.getElementById("usage-text");

  const usedPages = pagesUsed.size;
  const freePages = numPages - usedPages;
  const usagePercent = Math.round((usedPages / numPages) * 100);

  usageBar.style.width = `${usagePercent}%`;
  usageText.innerHTML = `${usedPages} used / ${numPages} total (${usagePercent}%)`;
}

// initialize the memory display
function initMemoryDisplay() {
  const memoryDisplay = document.getElementById("memory");

  for (let i = 0; i < memorySize; i++) {
    // create a new row for every 16 bytes
    if (i % pageSize === 0) {
      const row = document.createElement("div");
      row.classList.add("memory-row");

      // create a new address cell for the row
      const addressCell = document.createElement("div");
      addressCell.classList.add("memory-address");
      addressCell.innerHTML = `0x${i.toString(16).padStart(2, "0")}`;

      row.appendChild(addressCell);
      memoryDisplay.appendChild(row);
    }

    // create a new cell for each byte of memory
    const cell = document.createElement("div");
    cell.classList.add("memory-cell");
    cell.dataset.address = i;
    cell.innerHTML = memory[i];

    // add an event listener to update the cell value when clicked
    cell.addEventListener("click", () => {
      const value = parseInt(prompt("Enter a value for this memory cell:", cell.innerHTML), 10);
      if (!isNaN(value)) {
      cell.innerHTML = value;
      memory[i] = value;
      }
      });
 // add the cell to the current row
const currentRow = memoryDisplay.lastChild;
currentRow.appendChild(cell);

}
}

// initialize the usage bar
function initUsageBar() {
const usageBarFill = document.getElementById("usage-bar-fill");
usageBarFill.style.width = "0%";
}

// initialize the memory subsystem
function initMemory() {
initMemoryDisplay();
initUsageBar();
}

// add an event listener to the load button
const loadButton = document.getElementById("load-button");
loadButton.addEventListener("click", () => {
const program = [
0x48,
0x65,
0x6c,
0x6c,
0x6f,
0x20,
0x57,
0x6f,
0x72,
0x6c,
0x64,
0x21,
]; // "Hello World!" program
loadProgram(program);
});

// add an event listener to the unload button
const unloadButton = document.getElementById("unload-button");
unloadButton.addEventListener("click", unloadProgram);

// initialize the memory subsystem when the page loads
window.addEventListener("load", initMemory);