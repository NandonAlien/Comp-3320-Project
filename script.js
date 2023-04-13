const memory = new Array(256).fill(null);
let programLoaded = false;

// Calculate the current memory usage
function calculateUsage() {
  let used = 0;
  for (let i = 0; i < memory.length; i++) {
    if (memory[i] !== null) {
      used++;
    }
  }
  return used / memory.length;
}

// Render the memory display
function renderMemory() {
  const memoryEl = document.getElementById('memory');
  memoryEl.innerHTML = '';
  for (let i = 0; i < memory.length; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    if (memory[i] !== null) {
      cell.textContent = memory[i].toString(16).padStart(2, '0').toUpperCase();
    }
    cell.addEventListener('click', () => {
      if (programLoaded) {
        return;
      }
      const val = prompt(`Enter a value for address ${i.toString(16).toUpperCase().padStart(2, '0')}:`);
      if (val === null) {
        return;
      }
      const parsedVal = parseInt(val, 16);
      if (isNaN(parsedVal) || parsedVal < 0 || parsedVal > 255) {
        alert('Invalid value!');
        return;
      }
      memory[i] = parsedVal;
      renderMemory();
    });
    memoryEl.appendChild(cell);
  }
// Render the usage display
function renderUsage() {
    const usageBarEl = document.getElementById('usage-bar-fill');
    const usageTextEl = document.getElementById('usage-text');
    const usage = calculateUsage();
    usageBarEl.style.width = '${usage * 100}%';
    usageTextEl.textContent = '${Math.round(usage * 100)}%';
    }
    
    // Load a program into memory
    function loadProgram() {
    if (programLoaded) {
    alert('A program is already loaded!');
    return;
    }
    const program = prompt('Enter a program (up to 256 bytes) in hexadecimal:');
    if (program === null) {
    return;
    }
    const programBytes = program.match(/[0-9A-Fa-f]{2}/g);
    if (programBytes === null || programBytes.length > 256) {
    alert('Invalid program!');
    return;
    }
    for (let i = 0; i < programBytes.length; i++) {
    const val = parseInt(programBytes[i], 16);
    memory[i] = val;
    }
    programLoaded = true;
    renderMemory();
    renderUsage();
    }
    
    // Unload the current program from memory
    function unloadProgram() {
    if (!programLoaded) {
    alert('No program is currently loaded!');
    return;
    }
    for (let i = 0; i < memory.length; i++) {
    memory[i] = null;
    }
    programLoaded = false;
    renderMemory();
    renderUsage();
    }
    
    // Initialize the page
    function init() {
    renderMemory();
    renderUsage();
    document.getElementById('load').addEventListener('click', loadProgram);
    document.getElementById('unload').addEventListener('click', unloadProgram);
    }
    
    // Start the program
    init();
}   